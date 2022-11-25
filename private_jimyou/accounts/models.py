from re import S
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'
    
class Profile(models.Model):
    user = models.CharField(max_length=30)
    gender = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    favorite_words = models.CharField(max_length=50, blank=True)
    class Meta:
        verbose_name_plural = 'Profile'





# https://hodalog.com/how-to-extend-django-user-model/
# https://www.maytisk.com/django-login/
# (venv_jimyou_app) C:\Users\karin09\venv_jimyou_app\private_jimyou>python manage.py createsuperuser
# ユーザー名: postgres
# メールアドレス: karin0214sp@gmail.com
# Password:
# Password (again):
# このパスワードは メールアドレス と似すぎています。
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.
# https://github.com/knakajima3027/User-login-sample/blob/master/accounts/forms.py