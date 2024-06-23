from django.db import models


class Review(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    score = models.IntegerField()
