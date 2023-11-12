from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import HomeClientView, HomeDriverView

urlpatterns = [
    path("", HomeClientView.as_view(), name="client"),
    path("driver/", HomeDriverView.as_view(), name="driver"),
]
