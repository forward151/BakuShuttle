from django.db import models
from users.models import User
# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.address}"

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"