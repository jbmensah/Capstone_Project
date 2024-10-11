from rest_framework.test import APITestCase
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