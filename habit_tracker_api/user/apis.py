from rest_framework import views, response, exceptions, permissions

from . import serializer as user_serializer
from . import services, authentication

class RegisterApi(views.APIView):
	pass

	def post(self, request):
		serializer = user_serializer.UserSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		data = serializer.validated_data
		serializer.instance = services.create_user(user_dc=data)

		print(data)

		return response.Response(data=serializer.data)


class LoginApi(views.APIView):
	def post(self, request):
		email = request.data["email"]
		password = request.data["password"]

		user = services.user_email_selector(email=email)

		if user is None:
			raise exceptions.AuthenticationFailed("Invalid Credentials") # for security reasons

		if not user.check_password(raw_password=password):
			raise exceptions.AuthenticationFailed("Invalid Credentials") # for security reasons

		token = services.create_toke(user_id=user.id)

		resp = response.Response()

		resp.set_cookie(key="jwt", value=token, httponly=True)

		return resp


class UserApi(views.APIView):
	"""
	The endpoint can only be used if the user is authenticated
	"""
	authentication_classes = (authentication.CustomrUserAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request):		
		user = request.user
		serializer = user_serializer.UserSerializer(user)

		return response.Response(data=serializer.data)


class LogoutApi(views.APIView):
	authentication_classes = (authentication.CustomrUserAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request):
		resp = response.Response()
		resp.delete_cookie("jwt")
		resp.data = {"message": "Goodbye!!"}

		return resp