from django.contrib import admin
from .models import CustomUser
# Register your models here.


admin.site.site_header = "Habit Tracker Admin"
admin.site.site_title = "Habit Tracker Admin Portal"
admin.site.index_title = "Welcome to Habit Tracker Portal"
admin.site.register(CustomUser)
# admin.site.register(Habit)
