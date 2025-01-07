from django.db import models


class CompanyInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "CompanyInfo"
