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
def iindex(request):
    reviews = Review.objects.all()
    return render(request, "iindex.html", {"reviews": reviews})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        review = Review()
        review.name = request.user.first_name
        review.description = request.POST.get("description")
        review.score = request.POST.get("score")
        review.save()
    return HttpResponseRedirect("/")
def edit(request, id):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return HttpResponseRedirect("/")
    try:
        review = Review.objects.get(id=id)

        if request.method == "POST":
            review.description = request.POST.get("description")
            review.score = request.POST.get("score")
            review.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"review": review})
    except Review.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete(request, id):
    try:
        review = Review.objects.get(id=id)
        review.delete()
        return HttpResponseRedirect("/")
    except Review.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")