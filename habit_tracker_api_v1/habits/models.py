from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # Assuming the User model will be created later

class Habit(models.Model):
	FREQUENCY_CHOICES = [
		('daily', 'Daily'),
		('weekly', 'Weekly'),
		('monthly', 'Monthly'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Will remove null=True, blank=True later
	name = models.CharField(max_length=255)
	description = models.TextField(default="",blank=True)
	start_date = models.DateField()
	frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
	
	# New fields for MVP
	reminder_time = models.TimeField(null=True, blank=True)  # Optional field
	streak = models.IntegerField(default=0)  # Track streak of habit completion
	is_active = models.BooleanField(default=True)  # Soft delete logic
	created_at = models.DateTimeField(auto_now_add=True)  # Automatically set at creation
	updated_at = models.DateTimeField(auto_now=True)  # Automatically update whenever the record is saved
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")

	# class Meta:
	# 	ordering = ['-created_at']

	def __str__(self):
		return self.name

	def increment_streak(self):
		"""Custom method to increment the habit streak."""
		self.streak += 1
		self.save()

	def reset_streak(self):
		"""Custom method to reset the habit streak."""
		self.streak = 0
		self.save()

	def deactivate(self):
		"""Soft delete: mark the habit as inactive instead of deleting."""
		self.is_active = False
		self.save()

	def activate(self):
		"""Reactivate a soft-deleted habit."""
		self.is_active = True
		self.save()
