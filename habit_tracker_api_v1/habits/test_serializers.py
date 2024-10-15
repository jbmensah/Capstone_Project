from django.test import TestCase
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from habits.models import Habit, HabitLog
from habits.serializers import HabitSerializer, HabitLogSerializer
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()  # Assuming you're using the CustomUser model

class HabitSerializerTest(TestCase):

	def setUp(self):
		# Create sample data for testing
		self.user = User.objects.create_user(email='test@example.com', password='password123')

		# Dates for testing
		self.future_date = timezone.now().date() + timedelta(days=1)
		self.past_date = timezone.now().date() - timedelta(days=1)

	def test_start_date_in_the_past(self):
		"""Test that the start_date cannot be in the past during creation."""
		data = {
			'name': 'Morning Run',
			'description': 'Run every morning',
			'start_date': self.past_date,  # Start date in the past
			'end_date': None,
			'frequency': 'daily',
		}
		serializer = HabitSerializer(data=data)
		
		with self.assertRaises(ValidationError) as context:
			serializer.is_valid(raise_exception=True)
		
		self.assertIn('Start date cannot be in the past.', str(context.exception))

	def test_end_date_before_start_date(self):
		"""Test that end_date cannot be before start_date."""
		data = {
			'name': 'Morning Run',
			'description': 'Run every morning',
			'start_date': self.future_date,
			'end_date': self.past_date,  # End date before start date
			'frequency': 'daily',
		}
		serializer = HabitSerializer(data=data)

		with self.assertRaises(ValidationError) as context:
			serializer.is_valid(raise_exception=True)

		self.assertIn('End date must be after start date.', str(context.exception))

	def test_valid_habit_creation(self):
		"""Test a valid habit creation."""
		data = {
			'name': 'Morning Run',
			'description': 'Run every morning',
			'start_date': self.future_date,
			'end_date': None,  # No end date
			'frequency': 'daily',
		}
		serializer = HabitSerializer(data=data)
		self.assertTrue(serializer.is_valid())

	def test_invalid_frequency(self):
		"""Test that frequency must be one of the allowed choices."""
		data = {
			'name': 'Morning Run',
			'description': 'Run every morning',
			'start_date': self.future_date,
			'end_date': None,
			'frequency': 'yearly',  # Invalid frequency
		}
		serializer = HabitSerializer(data=data)

		with self.assertRaises(ValidationError) as context:
			serializer.is_valid(raise_exception=True)

		self.assertIn('Frequency must be daily or weekly.', str(context.exception))


class HabitLogSerializerTest(TestCase):

	def setUp(self):
		# Sample habit for testing logs
		self.user = User.objects.create_user(email='test@example.com', password='password123')
		self.habit = Habit.objects.create(
			user=self.user,
			name='Morning Run',
			description='Run every morning',
			start_date=timezone.now().date(),
			frequency='daily'
		)

	def test_valid_log_creation(self):
		"""Test creating a valid habit log entry."""
		data = {
			'habit': self.habit.id,
			'log_date': timezone.now().date(),
			'status': 'completed',
			'note': 'Felt great today!',
		}
		serializer = HabitLogSerializer(data=data)
		self.assertTrue(serializer.is_valid())

	def test_invalid_status(self):
		"""Test that status must be 'completed' or 'missed'."""
		data = {
			'habit': self.habit.id,
			'log_date': timezone.now().date(),
			'status': 'skipped',  # Invalid status
		}
		serializer = HabitLogSerializer(data=data)

		with self.assertRaises(ValidationError) as context:
			serializer.is_valid(raise_exception=True)

		self.assertIn('is not a valid choice', str(context.exception))
