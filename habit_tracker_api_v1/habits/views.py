from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from rest_framework.pagination import PageNumberPagination
from .models import Habit, HabitLog
from .serializers import HabitSerializer, HabitLogSerializer
from django.shortcuts import get_object_or_404
from accounts.serializers import CurrentUserHabitsSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(
	operation_summary="Homepage Summary",
	operation_description="Provides a summary of the logged-in user's habits, including total habits, active habits, current streaks, and recent habits."
)
def homepage(request: Request):
	user = request.user

	# Example stats for authenticated user
	user_habits = Habit.objects.filter(user=user)
	total_habits = user_habits.count()
	active_habits = user_habits.filter(is_active=True).count()
	current_streaks = sum(habit.streak for habit in user_habits)

	response = {
		"message": f"Welcome back, {user.username}!",
		"description": "Here's a summary of your progress:",
		"data": {
			"total_habits": total_habits,
			"active_habits": active_habits,
			"current_streaks": current_streaks,
			"recent_habits": [
				{
					"name": habit.name,
					"streak": habit.streak,
					"last_updated": habit.updated_at
				} for habit in user_habits.order_by('-updated_at')[:3]
			]
		},
		"endpoints": {
			"create_habit": "/api/habits/create/",
			"list_habits": "/api/habits/",
			"retrieve_update_delete_habit": "/api/habits/<id>/",
			"view_user_habits": "/api/user/habits/"
		}
	}
	return Response(data=response, status=status.HTTP_200_OK)


class HabitListCreateView(generics.GenericAPIView,
						mixins.ListModelMixin,
						mixins.CreateModelMixin
):
	"""
	A view for creating and listing Habits
	"""
	serializer_class = HabitSerializer
	permission_classes = [IsAuthenticated]
	queryset = Habit.objects.all().order_by('-created_at')
	pagination_class = PageNumberPagination

	def perform_create(self, serializer):
		"""
		When a new habit is created, ensure it is linked to the logged-in user.
		"""
		user = self.request.user
		serializer.save(user=user)
		return super().perform_create(serializer)
	
	
	def get_queryset(self):
		"""
		Ensure the queryset is filtered by the logged-in user.
		"""
		return Habit.objects.filter(user=self.request.user).order_by('-created_at')
	
	@swagger_auto_schema(
		operation_summary="List all Habits",
		operation_description="List all Habits belonging to the logged-in user.",
	)
	def get(self, request:Request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
	
	@swagger_auto_schema(
		operation_summary="Create a new Habit",
		operation_description="This endpoint creates a new Habit for the logged-in user.",
		request_body=HabitSerializer,
		responses={
			201: openapi.Response(description="Habit created successfully."),
			400: openapi.Response(description="Invalid input or validation error.")
		}
	)
	def post(self, request:Request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
	
	


class HabitRetrieveUpdateDestroyView(generics.GenericAPIView,
									mixins.RetrieveModelMixin,
									mixins.UpdateModelMixin,
									mixins.DestroyModelMixin
):
	"""
	A view for retrieving, updating, and deleting Habits
	"""
	serializer_class = HabitSerializer
	queryset = Habit.objects.all()
	permission_classes = [IsAuthenticated]

	def get_object(self):
		"""
		Ensure that only habits belonging to the logged-in user can be accessed.
		"""
		habit = get_object_or_404(Habit, pk=self.kwargs['pk'], user=self.request.user)
		return habit

	@swagger_auto_schema(
		operation_summary="Retrieve a Habit",
		operation_description="Retrieve a Habit belonging to the logged-in user.",
	)
	def get(self, request:Request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	
	@swagger_auto_schema(
		operation_summary="Update a Habit",
		operation_description="Update the details of a specific Habit created by the logged-in user.",
		request_body=HabitSerializer,
		responses={
			200: openapi.Response(description="Habit updated successfully."),
			400: openapi.Response(description="Invalid input or validation error."),
		}
	)
	def put(self, request:Request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	@swagger_auto_schema(
		operation_summary="Delete a Habit",
		operation_description="Delete a specific Habit created by the logged-in user.",
		responses={
			204: openapi.Response(description="Habit deleted successfully."),
			404: openapi.Response(description="Habit not found or unauthorized.")
		}
	)
	def delete(self, request:Request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(
	operation_summary="Get Habits for Current User",
	operation_description="Retrieve all habits for the currently logged-in user.",
)
def get_habits_for_current_user(request:Request):
	"""
    A view to retrieve all habits for the logged-in user.
    """
	user = request.user
	habits = Habit.objects.filter(user=user).order_by('-created_at')
	serializer = CurrentUserHabitsSerializer(
		instance=user,
		context={'request':request})

	return Response(data=serializer.data, status=status.HTTP_200_OK)


	def get(self, request:Request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

class HabitLogCreateView(generics.CreateAPIView):
	queryset = HabitLog.objects.all()
	serializer_class = HabitLogSerializer
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(
		operation_summary="Create a Habit Log Entry",
		operation_description="Log a habit entry for a specific Habit belonging to the logged-in user.",
		request_body=HabitLogSerializer,
		responses={
			201: openapi.Response(description="Habit log created successfully."),
			400: openapi.Response(description="Invalid input or validation error.")
		}
	)
	def perform_create(self, serializer):
		habit = serializer.validated_data['habit']
		habit.log_habit(status=serializer.validated_data['status'], note=serializer.validated_data.get('note'))
