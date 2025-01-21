from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='partner_logos/')
    url = models.URLField()
