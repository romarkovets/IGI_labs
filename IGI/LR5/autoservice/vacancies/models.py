from django.db import models


class Vacancy(models.Model):
    position = models.TextField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.position
