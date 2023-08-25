from django.db import models


class Mix(models.Model):
    STEM_CHOICES = [
        (0, '0-50 stems'),
        (1, '50-100 stems'),
    ]
    DAYS_CHOICES = [
        (1, '1-5 days'),
        (2, '6-10 days'),
        (3, '11-15 days'),
    ]
    number_of_stems = models.PositiveIntegerField(choices=STEM_CHOICES)
    number_of_days = models.PositiveIntegerField(choices=DAYS_CHOICES)
