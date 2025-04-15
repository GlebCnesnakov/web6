from django.db import models
from django.db.models import TextField


# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

class Employee(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='staff/', blank=True, null=True, verbose_name='Фото')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"