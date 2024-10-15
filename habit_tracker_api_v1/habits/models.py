# from django.utils.timezone import now
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # Assuming the User model will be created later

class Habit(models.Model):
	FREQUENCY_CHOICES = [
		('daily', 'Daily'),
		('weekly', 'Weekly'),		
	]


	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits") # Check if related_name is ok
	name = models.CharField(max_length=255)
	description = models.TextField(default="",blank=True)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)
	frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
	# target_days = models.CharField(max_length=255, blank=True, choices=DAYS_OF_WEEK)
	# New fields for MVP
	# reminder_time = models.TimeField(null=True, blank=True)  # Optional field
	streak = models.IntegerField(default=0)  # Track streak of habit completion
	is_active = models.BooleanField(default=True)  # Soft delete logic
	created_at = models.DateTimeField(auto_now_add=True)  # Automatically set at creation
	updated_at = models.DateTimeField(auto_now=True)  # Automatically update whenever the record is saved	

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

	def log_habit(self, status, note=None):
		"""Log the habit completion or miss. Prevent multiple logs for the same day."""
		log_entry, created = HabitLog.objects.get_or_create(
			habit=self,
			log_date= timezone.now().date(),
			defaults={'status': status, 'note': note}
		)
		
		if not created:
			# Optionally, update the log entry if needed
			log_entry.status = status
			log_entry.note = note
			log_entry.save()

		if status == 'completed':
			self.increment_streak()
		else:
			self.reset_streak()

	

class HabitLog(models.Model):
	STATUS_COMPLETED = 'completed'
	STATUS_MISSED = 'missed'
	
	STATUS_CHOICES = [
		(STATUS_COMPLETED, 'Completed'),
		(STATUS_MISSED, 'Missed'),
	]	
	
	habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
	log_date = models.DateField(default=timezone.now)  # Date the habit was logged
	status = models.CharField(max_length=20, choices=[('completed', 'Completed'), ('missed', 'Missed')])
	note = models.TextField(blank=True, null=True)  # Optional note for the log entry
	created_at = models.DateTimeField(auto_now_add=True)  # Log creation timestamp
	updated_at = models.DateTimeField(auto_now=True)  # Log update timestamp

	class Meta:
		ordering = ['-log_date']
		unique_together = ('habit', 'log_date') 

	def __str__(self):
		return f"{self.habit.name} - {self.log_date} ({self.status})"