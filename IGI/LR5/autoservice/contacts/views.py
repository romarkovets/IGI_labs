from django.shortcuts import render

from .models import Employee


# Create your views here.

def contacts_view(request):
    employees = Employee.objects.all()
    return render(request, 'contacts.html', {"employees": employees})

