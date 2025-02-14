from datetime import timezone
from email.policy import default
from django.utils import timezone
from django.db import models



# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text