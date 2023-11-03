from django.contrib import admin
from .models import Favorite
# Register your models here.


@admin.register(Favorite)
class Favorite(admin.ModelAdmin):
    fields = ["user", "address", "description"]