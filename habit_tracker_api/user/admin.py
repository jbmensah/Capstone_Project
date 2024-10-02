from django.contrib import admin

from . import models

class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(models.User, UserAdmin)

