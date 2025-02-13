from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }
        )
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }
        )
    )
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'X@X.X'
            }
        )
    )
    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '+375 (29) XXX-XX-XX'
            }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }
        )
    )

    date_of_birth = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Введите дату рождения'
            }
        )
    )

    is_employee = forms.ChoiceField(
        label='Статус',
        choices=((False, "Покупатель"), (True, "Работник"))
    )

    usable_password = None

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name',
                  'email', 'phone', 'date_of_birth', 'is_employee')
