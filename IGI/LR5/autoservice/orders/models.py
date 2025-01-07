from django.db import models

from services.models import Service
from users.models import Customer, Employee


# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, blank=True)

