from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from rest_framework.pagination import PageNumberPagination
from .models import Habit
from .serializers import HabitSerializer
from django.shortcuts import get_object_or_404
from accounts.serializers import CurrentUserHabitsSerializer


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
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
	
	def get(self, request:Request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
	
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

	def get(self, request:Request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	
	def put(self, request:Request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	def delete(self, request:Request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
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


class ListHabitsForAuthor(
	generics.GenericAPIView,
	mixins.ListModelMixin
):
	queryset = Habit.objects.all()
	serializer_class = HabitSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		# user = self.request.user
		# username = self.kwargs['username'] ===
		username = self.request.query_params.get('username') or None

		queryset = Habit.objects.all()

		if username is not None:
			return Habit.objects.filter(user__username=username)
		# return Habit.objects.filter(user=user) logged in user
		# return Habit.objects.filter(user__username=username) ===
		return queryset

	def get(self, request:Request, *args, **kwargs):
		return self.list(request, *args, **kwargs)