from django.db import models
from django.db.models import FloatField, DecimalField
from django.core.validators import MaxValueValidator, MinValueValidator


class Songs(models.Model):
    name = models.CharField(max_length=255)
    duration = models.DecimalField(max_digits=12, decimal_places=2)
    artist = models.CharField(max_length=255)

    def earnings_float(self):
        return float(self.duration)

    def __str__(self):
        return self.name
