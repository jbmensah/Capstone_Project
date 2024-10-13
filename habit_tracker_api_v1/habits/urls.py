from . import views
from django.urls import path

urlpatterns = [
	path("homepage/", views.homepage, name="habits_home"),
	path("", views.HabitListCreateView.as_view(), name="list_habits"),
	path("<int:pk>/", views.HabitRetrieveUpdateDestroyView.as_view(), name="habit_detail"),
	path("current_user/", views.get_habits_for_current_user, name="current_user"),
	# path("habits_for/", views.ListHabitsForAuthor.as_view(), name="habits_for_current_user"),
	path("habit_logs/", views.HabitLogCreateView.as_view(), name="create_habit_log"),
]