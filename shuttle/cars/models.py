from django.db import models
# Create your models here.


class Car(models.Model):
    model = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to="cars", null=True, blank=True)

    def __str__(self):
        return f"{self.model} - {self.number}"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
