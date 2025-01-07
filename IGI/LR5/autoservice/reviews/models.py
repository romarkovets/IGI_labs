from django.db import models
from datetime import date
from users.models import CustomUser

class Review(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateField(default=date.today)
