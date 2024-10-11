from django.utils import timezone
from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Habit
		fields = [
			'id',               # Include the ID field
			'user',             # The associated user (optional)
			'name',
			'description',
			'start_date',       # Validate this field. Should not be less that the current date
			'frequency',
			'reminder_time',
			'streak',
			'is_active',
			'created_at',      # Automatically managed fields
			'updated_at',
		]
		read_only_fields = ('created_at', 'updated_at')  # Make these fields read-only

	def validate_start_date(self, value):
		"""Custom validation for start_date to check it's not in the past."""
		# Ensure the start_date is not in the past ONLY during creation.
		if self.instance is None and value < timezone.now().date():
			raise serializers.ValidationError("Start date cannot be in the past.")
		return value

	def validate(self, attrs):
		"""Custom validation to ensure certain conditions are met."""
		if attrs.get('frequency') not in dict(Habit.FREQUENCY_CHOICES):
			raise serializers.ValidationError({"frequency": "Frequency must be daily, weekly, or monthly."})
		
		return attrs

	def create(self, validated_data):
		"""Custom create method to handle additional logic."""
		# Validate start_date (should not be in the past)
	
		return super().create(validated_data)

	def update(self, instance, validated_data):
		"""Custom update method to handle additional logic."""
		# Optionally handle any additional logic here before updating
		return super().update(instance, validated_data)
