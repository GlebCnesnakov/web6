from django.db import models
from django.db.models import TextField


# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=20, unique=True)

class Employee(models.Model):
    name = models.CharField(max_length=40)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)