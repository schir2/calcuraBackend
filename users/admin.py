import django.contrib.auth.admin
from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(django.contrib.auth.admin.UserAdmin):
    ...