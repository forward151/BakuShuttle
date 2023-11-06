from django.contrib import admin
from .models import History
# Register your models here.


@admin.register(History)
class History(admin.ModelAdmin):
    list_display = ["client", "driver", "address_from", "address_to", "date", "total_price"]


