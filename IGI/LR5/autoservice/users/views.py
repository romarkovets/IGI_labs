from datetime import datetime
import re


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from .models import CustomUser
import logging
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                logging.info(f"{user.username} вошел в аккаунт")
                login_user(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/')
            else:
                msg = 'invalid info'
                messages.success(request, "Ошибка, неправильный логин или пароль, повторите попытку!")
                return redirect('.')
            # return redirect('/')
        else:
            msg = 'error valid form'

    return render(request, 'login.html', {'form': form, 'msg': msg})


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            # address = request.POST.get('address', '')
            # telephone = request.POST.get('tel', '')
            # PHONE_NUMBER_REGEX = r"^\+375(\s+)?\(?(17|29|33|44)\)?(\s+)?[0-9]{3}-[0-9]{2}-[0-9]{2}$"
            # if not re.match(PHONE_NUMBER_REGEX, telephone):
            #     form.add_error('username', 'Некорректный формат телефонного номера')
            #     return render(request, 'users/registration.html', {'form': form, 'msg': 1})
            #
            # date_of_birth = form.cleaned_data.get('date_of_birth')
            # user_age = calculate_age(date_of_birth)
            # if user_age < 18:
            #     form.add_error('date_of_birth', 'Вам нет 18!')
            #     return render(request, 'users/registration.html', {'form': form, 'msg': 1})

            # user.is_customer = True
            user.save()
            # logging.info(f"{user.username} зарегистрирован")
            return redirect('/login')
    logging.info(f"Вызвана страница регистрации")
    return render(request, 'registration.html', {'form': form, 'msg': 1})


@login_required
def _logout(request):
    logging.info(f"{request.user.username} вышел из аккаунта")
    logout(request)
    return redirect('/')