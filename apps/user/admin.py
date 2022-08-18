from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):

    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "last_login",
    ]

    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "date_joined",
        "last_login",
        "groups",
        "user_permissions",
    ]
