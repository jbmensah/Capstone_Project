from rest_framework.test import APITestCase
from .views import HabitListCreateView
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model 



class HelloWorldTestCase(APITestCase):

	def setUp(self):
		# Use get_user_model() to access your CustomUser model
		self.user = get_user_model().objects.create_user(
			email="testuser@example.com", 
			password="testpassword"
		)
		self.client.force_authenticate(user=self.user)  # Authenticate the user for the test

	def test_hello_world(self):
		response = self.client.get(reverse("habits_home"))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["message"], "Hello, World!")

class HabitListCreateTestCase(APITestCase):

	def setUp(self):
		# Set up the authenticated user
		self.user = get_user_model().objects.create_user(
			email="testuser@example.com",
			password="testpassword"
		)
		self.client.force_authenticate(user=self.user)  # Authenticate the user for the test
		self.url = reverse("list_habits")

	def test_list_habits(self):
		# Use self.client.get() to ensure authentication is handled
		response = self.client.get(self.url)
		
		print(response.data)
		# Assert the response status code
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["count"], 0)
		self.assertEqual(len(response.data["results"]), 0)

	def test_habit_creation(self):
		sample_habit = {"name": "Test Habit",
						"description": "This is a test habit",
						"frequency": "daily",
						"start_date": "2024-10-11"}
		response = self.client.post(self.url, sample_habit, format="json")
		
		# print(response.data)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data["name"], "Test Habit")

