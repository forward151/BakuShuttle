from django.db import models
from cars.models import Car


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.CharField()
    photo_user = models.ImageField(default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(max_length=5, decimal_places=1, max_digits=1)

    def __str__(self):
        return f"{self.user} - {self.rating}"

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_length=5, decimal_places=1, max_digits=1)

    def __str__(self):
        return f"{self.user} - {self.rating}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


