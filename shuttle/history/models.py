from django.db import models
from users.models import Client, Driver
# Create your models here.


class History(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    address_from = models.CharField()
    address_to = models.CharField()
    date = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.address_from} - {self.address_to} | {self.date}"

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "Histories"
