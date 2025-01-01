from django.shortcuts import render
from .models import Vacancy


def vacancies_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies': vacancies})
