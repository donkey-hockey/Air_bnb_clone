from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Field Set", {"fields": ("avatar", "gender", "bio")}),
    )
