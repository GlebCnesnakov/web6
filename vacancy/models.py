from django.db import models
from staff.models import Position
from django.utils import timezone
# Create your models here.

class Vacancy(models.Model):
    date = models.DateTimeField(default=timezone.now)
    position = models.ForeignKey(Position, models.CASCADE)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()