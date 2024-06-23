from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError()
        if not username:
            raise ValueError()

        user = self.model(email=self.normalize_email(email), username=username,
                          first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, first_name=None, last_name=None):
        user = self.create_user(username=username, email=email, password=password,
                                first_name=first_name, last_name=last_name)
        user.admin = True
        user.staff = True
        user.superuser = True
        user.save()
        return user
