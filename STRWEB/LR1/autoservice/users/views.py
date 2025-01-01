from datetime import datetime
import re
from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from .models import CustomUser, Employee, Customer
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
                login_user(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/')
            else:
                messages.success(request, "Ошибка, неправильный логин или пароль, повторите попытку!")
                return redirect('.')
        else:
            msg = 'error valid form'

    return render(request, 'login.html', {'form': form, 'msg': msg})


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            phone = request.POST.get('phone', '')
            PHONE_NUMBER_REGEX = r"^\+375\s\(29\)\s[0-9]{3}-[0-9]{2}-[0-9]{2}$"
            if not re.match(PHONE_NUMBER_REGEX, phone):
                form.add_error('phone', 'Некорректный формат телефонного номера')
                return render(request, 'registration.html', {'form': form, 'msg': 1})

            date_of_birth = form.cleaned_data.get('date_of_birth')
            user_age = calculate_age(date_of_birth)
            if user_age < 18:
                form.add_error('date_of_birth', 'Вам нет 18 лет')
                return render(request, 'registration.html', {'form': form, 'msg': 1})

            user = form.save(commit=False)

            user.save()

            if not user.is_employee:
                customer = Customer.objects.create(user=user)
                customer.save()
            else:
                is_employee = Employee.objects.create(user=user)
                is_employee.save()
            return redirect('/login')
    return render(request, 'registration.html', {'form': form, 'msg': 1})


@login_required
def _logout(request):
    logout(request)
    return redirect('/')


def calculate_age(birth_date: datetime):
    current_date = datetime.now().date()
    age = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (
            current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    return age




