from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.Create_Account.as_view(), name="create_account"),
    path('login/', views.Account_login.as_view(), name="login"),
]