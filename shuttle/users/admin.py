from django.contrib import admin
from .models import User, Driver, Client
# Register your models here.


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "photo_user"]


@admin.register(Driver)
class User(admin.ModelAdmin):
    list_display = ["user", "car", "rating"]


@admin.register(Client)
class User(admin.ModelAdmin):
    list_display = ["user", "rating"]
