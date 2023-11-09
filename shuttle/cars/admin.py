from django.contrib import admin
from .models import Car
# Register your models here.


@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = ["model", "number", "description", "photo"]