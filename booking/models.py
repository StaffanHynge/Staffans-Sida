from django.db import models


class BookMix(models.model):
    name = models.CharField(max_length=400)
    time = models.CharField(max_length=400)
    stems = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return (self.name)
