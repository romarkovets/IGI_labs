from django.db import models

from services.models import Service
from users.models import Customer, Employee


# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_received = models.BooleanField(default=False)

    @property
    def total_cost(self):
        return self.quantity * self.service.cost


