from django.shortcuts import render
from news.models import Article
from .models import Partner
from services.models import Service
import requests


def index(request):
    latest_news = Article.objects.latest('id')

    cat_api_data = get_cat_api()
    dog_api_data = get_dog_api()
    partners = Partner.objects.all()
    services = Service.objects.all()

    return render(request, "index.html", {"latest_news": latest_news,
                                          "cat_api_data": cat_api_data,
                                          "dog_api_data": dog_api_data,
                                          "partners": partners,
                                          "services": services})


def get_cat_api():
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_dog_api():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        return response.json()
    else:
        return None
