from django.conf import settings
from rest_framework import authentication, exceptions
import jwt

from . import models

class CustomrUserAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):
		token = request.COOKIES.get("jwt")

		if not token:
			return None

		try:
			payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
		except jwt.ExpiredSignatureError:
			raise exceptions.AuthenticationFailed("Unauthenticated")
		user = models.User.objects.filter(id=payload["id"]).first()
		return (user, None)