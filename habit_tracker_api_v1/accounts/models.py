from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("The email must be set")
		email = self.normalize_email(email) # Convert email to all lower case and valid email
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		extra_fields.setdefault("is_active", True)

		if extra_fields.get("is_staff") is not True:
			raise ValueError("Superuser must have is_staff=True.")
		if extra_fields.get("is_superuser") is not True:
			raise ValueError("Superuser must have is_superuser=True.")
		return self.create_user(email, password, **extra_fields)
	

class CustomUser(AbstractUser):
	email = models.EmailField(max_length=80, unique=True)
	username = models.CharField(max_length=150, unique=True, default="default_username")
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	objects = CustomUserManager()


	def __str__(self):
		return self.email