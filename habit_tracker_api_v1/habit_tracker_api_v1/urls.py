from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
openapi.Info(
	title="Habit Tracker API",
	default_version='v1',
	description="The Habit Tracker API allows users to create, manage, and track their habits. 	It provides features for habit logging, progress tracking, and streak management. This API supports operations such as creating habits, updating habit information, retrieving habit details, and deleting habits. It also includes user authentication and permission management, ensuring secure access to habit data. Additionally, users can view insights into their habit performance, including streaks, completion rates, and habit logs.",
),
public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
	path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path("admin/", admin.site.urls),
	path("habits/", include("habits.urls")),
	path("auth/", include("accounts.urls")),
]