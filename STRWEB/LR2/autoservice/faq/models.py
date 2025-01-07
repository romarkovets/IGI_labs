from django.db import models
from django.utils import timezone


class FAQ(models.Model):
    question = models.TextField(max_length=100)
    answer = models.TextField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question
