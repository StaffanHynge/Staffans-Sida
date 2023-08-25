from django.db import models
from django.contrib.auth.models import User


class BookMix(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    time = models.CharField(max_length=400)
    stems = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return (self.name)
