from django.db import models
from staff.models import Position
from django.utils import timezone


class Description(models.Model):
    text = models.TextField()

class Vacancy(models.Model):
    date = models.DateTimeField(default=timezone.now)
    position = models.ForeignKey(Position, models.CASCADE)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.OneToOneField(Description, on_delete=models.SET_NULL, null=True)