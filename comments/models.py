from datetime import timezone
from email.policy import default
from django.utils import timezone
from django.db import models

class PublishedAndSortedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True).order_by("-date")

    def __str__(self):
        return self.text

# Create your models here.
class Comment(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Не опубликовано'
        PUBLISHED = 1, 'Опубликовано'

    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50)
    is_active = models.BooleanField(default=Status.PUBLISHED, choices=Status.choices)
    objects = models.Manager()
    published = PublishedAndSortedModel()

