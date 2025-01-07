from django.shortcuts import render

from .models import Article


# Create your views here.

def news(request):
    all_news = Article.objects.all().order_by('-id')
    return render(request, 'news.html', {"news": all_news})


def article(request, id):
    _article = Article.objects.get(id=id)
    return render(request, 'article.html', {"article": _article})

