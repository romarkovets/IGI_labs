from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to="images/", default="images/default.jpg")
    list_of_jobs = models.CharField(max_length=200)

