from django.contrib import admin
from django.urls import path
from index.views import index
from users.views import login, registration

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="index"),
    path('login/', login, name="login"),
    path('registration/', registration, name="registration"),
    path("", index),
]