from django.shortcuts import render

# Create your views here.

def additional_view(request):
    return render(request, 'additional.html')