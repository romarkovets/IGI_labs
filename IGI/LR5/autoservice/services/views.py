from django.shortcuts import render
import re
from .models import Service
from .forms import SearchForm

def services_view(request):
    services = Service.objects.all()
    if "text" in request.GET:
        services = filter(lambda x: re.search(request.GET["text"], x.name), services)
    search_form = SearchForm()
    services = list(services)
    if "sorting" in request.GET and request.GET["sorting"] == "2":
        services.sort(key=lambda x: x.cost, reverse=True)
    else:
        services.sort(key=lambda x: x.cost)

    return render(request, 'services.html', {'services': services,
                                             "search_form": search_form})
