from django.contrib import admin
from .models import User, Driver, Client
# Register your models here.


@admin.register(User)
class User(admin.ModelAdmin):
    fields = ["first_name", "last_name", "mail", "phone", "photo_user"]


@admin.register(Driver)
class User(admin.ModelAdmin):
    fields = ["user", "car", "rating"]


@admin.register(Client)
class User(admin.ModelAdmin):
    fields = ["user", "rating"]
