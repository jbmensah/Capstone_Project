from rest_framework import serializers
from .models import User

from . import services

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name', 'email', 'password']
	# id = serializers.IntegerField(read_only=True)
	# first_name = serializers.CharField()
	# last_name = serializers.CharField()
	# email = serializers.EmailField()
	# password = serializers.CharField(write_only=True)

	def create(self, validated_data):
		return services.create_user(user_dc=services.UserDataClass(**validated_data))

	def to_internal_value(self, data):
		
		data = super().to_internal_value(data)
		
		return services.UserDataClass(**data)

	# def create(self, validated_data):
	# 	return self.User.objects.create(**validated_data)