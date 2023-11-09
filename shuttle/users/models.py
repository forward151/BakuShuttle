from django.db import models
from cars.models import Car
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    photo_user = models.ImageField(upload_to="avatars", blank=True, null=True, verbose_name="photo")
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name="phone")
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(max_length=5, decimal_places=1, max_digits=2)

    def __str__(self):
        return f"{self.user} - {self.rating}"

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_length=5, decimal_places=1, max_digits=2)

    def __str__(self):
        return f"{self.user} - {self.rating}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


