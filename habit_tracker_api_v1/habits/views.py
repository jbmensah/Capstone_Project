from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from .models import Habit
from .serializers import HabitSerializer
from django.shortcuts import get_object_or_404
from accounts.serializers import CurrentUserHabitsSerializer


# Create your views here.
@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):
	permission_classes = []

	if request.method == "POST":
		data = request.data

		response = {"message": "Hello, World!", "data":data}
		return Response(data=response, status=status.HTTP_201_CREATED)

	response = {"message": "Hello, World!"}
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
	queryset = Habit.objects.all()

	def perform_create(self, serializer):
		user = self.request.user
		serializer.save(author=user)
		return super().perform_create(serializer)

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

	def get(self, request:Request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	
	def put(self, request:Request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	def delete(self, request:Request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def get_habits_for_current_user(request:Request):
	user = request.user

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
			return Habit.objects.filter(author__username=username)
		# return Habit.objects.filter(author=user) logged in user
		# return Habit.objects.filter(author__username=username) ===
		return queryset

	def get(self, request:Request, *args, **kwargs):
		return self.list(request, *args, **kwargs)