from django.db import models

class Discounts(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    discount = models.IntegerField()