from django.urls import path
from . import views

app_name = 'jimyou'
urlpatterns = [
    path('', views.home_view, name="index"),
    path('home-page/', views.HomeView.as_view(), name="home-page"),
    path('services/', views.profile, name="services"),
    path('about-us/', views.AboutusView.as_view(), name="about-us"),
    path('about-me/', views.AboutmeView.as_view(), name="about-me"),
    path('contacts/', views.add, name="contacts"),
    path('hm/', views.HmView.as_view(), name="hm"),
    path('index-account/', views.Account_login.as_view(), name="index-account"),

]
