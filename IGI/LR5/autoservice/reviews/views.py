from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.

def new_review(request):
    reviews = Review.objects.all()
    form = None
    if request.user.is_authenticated:
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            review = form.save(commit=False)
            review.name = request.user.first_name + " " + request.user.last_name
            review.save()
            return redirect('/reviews')

    return render(request, 'reviews.html', {"reviews": reviews, "form": form})

def reviews_view(request):
    pass