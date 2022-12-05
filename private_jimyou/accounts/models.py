from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     """拡張ユーザーモデル"""
#     # email = models.EmailField(max_length=30, required=True)
#     # birthday = models.DateField(verbose_name='誕生日',null=True, blank=True)
#     # country = models.CharField(verbose_name='国籍',null=True, blank=True)
#     # gender = models.CharField(verbose_name='性別',null=True, blank=True)
#     class Meta:
#         verbose_name_plural = 'CustomUser'

# class test(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     gender = models.CharField(max_length=20, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     favorite_words = models.CharField(max_length=50, blank=True)
#     birthday = models.DateField(null=True, blank=True)
#     country = models.CharField(null=True, blank=True,max_length=256)
#     gender = models.CharField(null=True, blank=True,max_length=256)

class Usertest(AbstractUser):
    """拡張ユーザーモデル"""
    # email = models.EmailField(max_length=30, required=True)
    birthday = models.DateField(verbose_name='誕生日',null=True, blank=True)
    country = models.CharField(verbose_name='国籍',null=True, blank=True, max_length=50)
    gender = models.CharField(verbose_name='性別',null=True, blank=True, max_length=50)
    class Meta:
        verbose_name_plural = 'Usertest'
    REQUIRED_FIELDS = ["email", "birthday", "country", "gender"]






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