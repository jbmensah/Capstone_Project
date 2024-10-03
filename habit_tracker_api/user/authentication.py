from django.conf import settings
from rest_framework import authentication, exceptions
import jwt

from . import models

def verify_token(token: str) -> dict:
	"""
	Verify the JWT token and return the payload if valid.
	Raises AuthenticationFailed exception for invalid or expired tokens.
	"""
	try:
		payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
		return payload
	except jwt.ExpiredSignatureError:
		raise exceptions.AuthenticationFailed("Token has expired.")
	except jwt.DecodeError:
		raise exceptions.AuthenticationFailed("Token is invalid.")

class CustomUserAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):
		# Check the token in cookies or in the Authorization header
		token = request.COOKIES.get("jwt") or request.META.get("HTTP_AUTHORIZATION")

		if not token:
			return None

		# If using Authorization header, it should be prefixed with "Bearer "
		if token.startswith("Bearer "):
			token = token.split(" ")[1]  # Extract the token

		try:
			payload = verify_token(token)  # Use the verify_token function
		except exceptions.AuthenticationFailed as e:
			raise e  # Re-raise the exception for any authentication failures
		
		user = models.User.objects.filter(id=payload["id"]).first()
		return (user, None)
