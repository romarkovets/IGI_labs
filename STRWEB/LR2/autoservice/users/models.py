from datetime import date
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone


from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=20, primary_key=True, unique=True)
    id = models.IntegerField(default=1)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    phone = models.CharField(max_length=19, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    registration_date = models.DateField(default=timezone.now)
    date_of_birth = models.DateField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone']
    objects = CustomUserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (
                    today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        return None

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_age(self):
        return timezone.now() - self.registration_date

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_active(self):
        return self.active


class Employee(models.Model):
    photo = models.ImageField(upload_to="images/", default="images/default.jpg")
    list_of_jobs = models.CharField(max_length=200, default="Не определено") #поменять на список services
    #список orders?
    schedule = models.CharField(max_length=200, default="Не определено")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)