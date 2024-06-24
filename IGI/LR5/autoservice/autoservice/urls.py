from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from index.views import index
from users.views import login, registration, _logout
from news.views import news
from faq.views import faq
from vacancies.views import vacancies_view
from about.views import about_view
from privacy.views import privacy_view
from contacts.views import contacts_view

# from reviews.views import reviews_view
from reviews.views import iindex,create,edit,delete

from services.views import services_view
from discounts.views import discounts_view
from orders.views import employee_view, customer_view


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

    # path('reviews/', index, name="reviews"),
    path("reviews/", iindex),
    path("reviews/create/", create),
    path("reviews/edit/<int:id>/", edit),
    path("reviews/delete/<int:id>/", delete),


    path('services/', services_view, name="service"),
    path('employeeorders/', employee_view, name="employee_view"),
    path('customerorders/', customer_view, name="customer_view"),
    path('discounts/', discounts_view, name="discounts"),

    path("", index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
