from django.contrib import admin
from django.urls import path, include
# from habits.views import HabitViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("", HabitViewSet, basename="habits")

urlpatterns = [
	path("admin/", admin.site.urls),
	path("habits/", include("habits.urls")),
	path("auth/", include("accounts.urls")),
]