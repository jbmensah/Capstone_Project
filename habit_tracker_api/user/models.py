from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str = None) -> "User":
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True  # Default to active
        user.is_staff = False  # Default to not staff
        user.is_superuser = False  # Default to not superuser
        user.save()

        return user
    
    def create_superuser(self, first_name: str, last_name: str, email: str, password: str = None) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class User(AbstractUser):
    first_name = models.CharField(verbose_name='First Name', max_length=255)
    last_name = models.CharField(verbose_name='Last Name', max_length=255)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    username = None  # No username field

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['first_name']  # Example ordering
