from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    # email = models.EmailField(max_length=30, required=True)
    # birthday = models.DateField(verbose_name='誕生日',null=True, blank=True)
    # country = models.CharField(verbose_name='国籍',null=True, blank=True)
    # gender = models.CharField(verbose_name='性別',null=True, blank=True)
    class Meta:
        verbose_name_plural = 'CustomUser'

# class test(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     gender = models.CharField(max_length=20, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     favorite_words = models.CharField(max_length=50, blank=True)
#     birthday = models.DateField(null=True, blank=True)
#     country = models.CharField(null=True, blank=True,max_length=256)
#     gender = models.CharField(null=True, blank=True,max_length=256)



class Customprofile(models.Model):
    user_id = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
    user_birthday = models.DateField(verbose_name='誕生日',null=True, blank=True)
    COUNTRY_CHOICES = ((u'j', u'日本'),(u'a', u'アメリカ合衆国'),(u'c', u'中華人民共和国'),(u'u', u'ウクライナ'))
    user_country = models.CharField(max_length=3, default=u'日本',choices=COUNTRY_CHOICES)
    GENDER_CHOICES = ((u'M', u'Male'),(u'F', u'Female'),(u'N', u'未回答'))
    gender = models.CharField(max_length=2, default=u'未回答',choices=GENDER_CHOICES)




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