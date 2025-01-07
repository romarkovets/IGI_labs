from django.shortcuts import render
from .models import Discounts


def discounts_view(request):
    discounts = Discounts.objects.all()
    return render(request, 'discounts.html', {'discounts': discounts})
