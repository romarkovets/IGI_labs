from django.contrib import admin
from django.urls import path
from index.views import index
from users.views import login, registration, _logout
from news.views import news
from faq.views import faq
from vacancies.views import vacancies_view
from django.conf.urls.static import static
from django.conf import settings
from about.views import about_view
from privacy.views import privacy_view
from contacts.views import contacts_view
from reviews.views import new_review, reviews_view

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="index"),
    path('login/', login, name="login"),
    path('registration/', registration, name="registration"),
    path('logout/', _logout, name="_logout"),
    path('news/', news, name="news"),
    path('faq/', faq, name="faq"),
    path('vacancies/', vacancies_view, name="vacancies"),
    path('about/', about_view, name="about"),
    path('privacy/', privacy_view, name="privacy"),
    path('contacts/', contacts_view, name="contacts"),
    path('reviews/', new_review, name="new review"),

    path("", index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)