from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .tokens import create_jwt_pair_for_user
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class SignUpView(generics.GenericAPIView):	
	serializer_class = SignUpSerializer
	permission_classes = []

	@swagger_auto_schema(
		operation_summary="Create a new user account",  # Summary for quick understanding
		operation_description="""
			This endpoint allows new users to sign up by providing their details like email and password.
			The created user will then be able to log in to the system.
		""",
		request_body=SignUpSerializer,  # This helps to auto-generate the expected input body
		responses={
			201: openapi.Response(description="User created successfully"),
			400: openapi.Response(description="Validation error - user creation failed")
		}
	)
	def post(self, request:Request):
		data = request.data

		serializer = self.serializer_class(data=data)

		if serializer.is_valid():
			serializer.save()

			response = {
				"message": "Account created successfully.",
				"data":serializer.data
			}
			return Response(data=response, status=status.HTTP_201_CREATED)

		return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

class LoginView(APIView):
	permission_classes = [AllowAny]

	@swagger_auto_schema(
		operation_summary="Login user",  # Simple operation summary
		operation_description="""
			This endpoint authenticates a user by their email and password.
			If successful, it returns a JWT token pair (access and refresh tokens).
		""",
		request_body=openapi.Schema(
			type=openapi.TYPE_OBJECT,
			properties={
				'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
				'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
			},
			required=['email', 'password'],  # Ensure required fields are indicated
			example={
				'email': 'example@app.com',
				'password': '123456'
			}
		),
		responses={
			200: openapi.Response(
				description="Login successful",
				examples={
					"application/json": {
						"message": "Login successful.",
						"tokens": {
							"access": "jwt-access-token",
							"refresh": "jwt-refresh-token"
						}
					}
				}
			),

			201: openapi.Response(
		description="User created successfully",
		examples={
			"application/json": {
				"message": "Account created successfully.",
				"data": {
					"id": 1,
					"email": "example@app.com",
					"username": "example_user"
				}
			}
		}
	),
			
			400: openapi.Response(
				description="Invalid credentials",
				examples={
					"application/json": {
						"message": "Wrong credentials."
					}
				}
			)
		}
	)
	def post(self, request:Request):
		email = request.data.get("email")
		# username = request.data.get("username")
		password = request.data.get("password")

		user = authenticate(email=email, password=password)

		if user is not None:
			tokens = create_jwt_pair_for_user(user=user)
			response = {
				"message": "Login successful.",
				"tokens": tokens
			}
			return Response(data=response, status=status.HTTP_200_OK)
		else:
			return Response(data={"message": "Wrong credentials"}, status=status.HTTP_400_BAD_REQUEST)

	@swagger_auto_schema(
	operation_summary= "Get Current User Information",
	operation_description= "This endpoint retrieves the current authenticated user and their authorization token. It returns a 200 OK response with the user information if the request contains valid authentication. This can be useful for verifying user authentication status.",
	)
	def get(self, request:Request):
		content = {
			"user": str(request.user),
			"auth": str(request.auth),
		}

		return Response(data=content, status=status.HTTP_200_OK)