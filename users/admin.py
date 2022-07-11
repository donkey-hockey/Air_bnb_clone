from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from rooms import models as room_models


class RoomInline(admin.TabularInline):
    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    inlines = (RoomInline,)
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Field Set", {"fields": ("avatar", "gender", "bio")}),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
