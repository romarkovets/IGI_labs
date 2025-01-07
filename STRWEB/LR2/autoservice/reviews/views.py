from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


# def reviews_view(request):
#     reviews = Review.objects.all()
#     form = None
#     if request.user.is_authenticated:
#         form = ReviewForm(request.POST or None)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.name = request.user.first_name + " " + request.user.last_name
#             review.save()
#             return redirect('/reviews')
#
#     return render(request, 'reviews.html', {"reviews": reviews, "form": form})
def review_index(request):
    reviews = Review.objects.all()
    return render(request, "review_index.html", {"reviews": reviews})


def review_create(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")
    if request.method == "POST":
        review = Review()
        review.name = request.user.first_name
        review.description = request.POST.get("description")
        review.score = request.POST.get("score")
        review.user = request.user
        review.save()
        return HttpResponseRedirect("/reviews")
    else:
        return render(request, "review_create.html", {'form': ReviewForm()})


def review_edit(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    try:
        review = Review.objects.get(id=id)
        if review.user != request.user and not request.user.is_superuser:
            return HttpResponseNotFound("<h2>Review not found</h2>")

        if request.method == "POST":
            review.description = request.POST.get("description")
            review.score = request.POST.get("score")
            review.save()
            return HttpResponseRedirect("/reviews")
        else:
            return render(request, "review_edit.html", {"review": review, 'form': ReviewForm()})
    except Review.DoesNotExist:
        return HttpResponseNotFound("<h2>Review not found</h2>")


def review_delete(request, id):
    try:
        review = Review.objects.get(id=id)
        if review.user != request.user and not request.user.is_superuser:
            return HttpResponseNotFound("<h2>Review not found</h2>")
        review.delete()
        return HttpResponseRedirect("/reviews")
    except Review.DoesNotExist:
        return HttpResponseNotFound("<h2>Review not found</h2>")