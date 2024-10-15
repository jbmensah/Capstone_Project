from django.utils import timezone
from rest_framework import serializers
from .models import Habit, HabitLog

class HabitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Habit
		fields = [
			'id',               # Include the ID field
			'user',             # The associated user (optional)
			'name',
			'description',
			'start_date',       # Validate this field.
			'end_date',         # Validate this field.
			'frequency',
			'streak',
			'is_active',
			'created_at',       # Automatically managed fields
			'updated_at',
		]
		read_only_fields = ('id', 'user', 'streak', 'created_at', 'updated_at')

	def validate_start_date(self, value):
		"""Ensure start_date is not in the past during creation."""
		if self.instance is None and value < timezone.now().date():
			raise serializers.ValidationError("Start date cannot be in the past.")
		return value

	def validate(self, attrs):
		"""Custom validation to ensure start_date is before end_date."""
		start_date = attrs.get('start_date', self.instance.start_date if self.instance else None)
		end_date = attrs.get('end_date', None)

		# Ensure that the start_date is before the end_date if end_date is provided.
		if end_date and start_date and end_date < start_date:
			raise serializers.ValidationError({
				"end_date": "End date must be after start date."
			})

		return super().validate(attrs)

class HabitLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = HabitLog
		fields = ['id', 'habit', 'log_date', 'status', 'note', 'created_at', 'updated_at']
		read_only_fields = ['id', 'created_at', 'updated_at']
