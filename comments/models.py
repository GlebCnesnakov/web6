from datetime import timezone
from email.policy import default
from django.utils import timezone
from django.db import models

class PublishedAndSortedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True).order_by("-date")

    def __str__(self):
        return self.text


class Comment(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Не опубликовано'
        PUBLISHED = 1, 'Опубликовано'

    text = models.TextField(verbose_name='текст')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    author = models.CharField(max_length=50, verbose_name='Автор')
    is_active = models.BooleanField(default=Status.PUBLISHED, choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), verbose_name='Опубликован')
    objects = models.Manager()
    published = PublishedAndSortedModel()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комменатрии'
