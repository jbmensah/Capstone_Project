from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(max_length=80)
	username = serializers.CharField(max_length=45)
	password = serializers.CharField(min_length=8, write_only=True)	
	class Meta:
		model = CustomUser
		fields = ('email', 'username', 'password')

	def validate(self, attrs):
		email_exists = CustomUser.objects.filter(email=attrs['email']).exists()
		username_exists = CustomUser.objects.filter(username=attrs['username']).exists()

		if email_exists:
			raise ValidationError("Email already exists")

		if username_exists:
			raise ValidationError("Username already exists")

		return super().validate(attrs)


	def create(self, validated_data):
		password = validated_data.pop('password')
		user = super().create(validated_data)

		user.set_password(password)
		user.save()

		# Create an authentication token for the new user
		Token.objects.create(user=user)
		return user
	
class CurrentUserHabitsSerializer(serializers.ModelSerializer):
	# habits = serializers.StringRelatedField(many=True, read_only=True)
	habits = serializers.HyperlinkedRelatedField(
		many=True,
		view_name = 'habit_detail',
		queryset = CustomUser.objects.all()
	)

	class Meta:
		model = CustomUser
		fields = ['id', 'username', 'email', 'habits']