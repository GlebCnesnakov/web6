from django.db import models
from staff.models import Position
from django.utils import timezone


class Description(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описания"

class Vacancy(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    position = models.ForeignKey(Position, models.CASCADE, verbose_name='Должность')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    description = models.OneToOneField(Description, on_delete=models.SET_NULL, null=True, verbose_name='Описание')

    def __str__(self):
        return self.position.name
    

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'