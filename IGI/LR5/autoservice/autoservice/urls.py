from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from index.views import index
from users.views import login, registration, _logout
from news.views import news, article
from faq.views import faq
from vacancies.views import vacancies_view
from about.views import about_view
from privacy.views import privacy_view
from contacts.views import contacts_view

# from reviews.views import reviews_view
from reviews.views import review_index, review_create, review_edit, review_delete

from services.views import services_view
from discounts.views import discounts_view
from orders.views import customer_view


urlpatterns = [
    path('admin/', admin.site.urls, name="index"),
    path('login/', login, name="login"),
    path('registration/', registration, name="registration"),
    path('logout/', _logout, name="_logout"),
    path('news/', news, name="news"),
    path('article/<int:id>', article, name="article"),
    path('faq/', faq, name="faq"),
    path('vacancies/', vacancies_view, name="vacancies"),
    path('about/', about_view, name="about"),
    path('privacy/', privacy_view, name="privacy"),
    path('contacts/', contacts_view, name="contacts"),

    # path('reviews/', index, name="reviews"),
    path("reviews/", review_index),
    path("reviews/create/", review_create),
    path("reviews/edit/<int:id>/", review_edit),
    path("reviews/delete/<int:id>/", review_delete),


    path('services/', services_view, name="service"),
    path('customerorders/', customer_view, name="customer_view"),
    path('discounts/', discounts_view, name="discounts"),

    path("", index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
