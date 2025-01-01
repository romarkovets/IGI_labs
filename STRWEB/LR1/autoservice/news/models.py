from django.db import models

# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images/", default="images/default.jpg")
    text = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Article"
        get_latest_by = ['title']
