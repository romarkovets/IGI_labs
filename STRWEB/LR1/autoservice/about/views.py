from django.shortcuts import render
from .models import CompanyInfo


# Create your views here.
def about_view(request):
    company_infos = CompanyInfo.objects.all()
    return render(request, 'about.html', {"company_infos": company_infos})
