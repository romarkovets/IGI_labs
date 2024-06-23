from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images/", default="images/default.jpg")

    class Meta:
        verbose_name_plural = "Article"
        get_latest_by = ['title']
