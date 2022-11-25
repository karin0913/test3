from django.urls import path,include

from . import views


app_name = 'jimyou'
urlpatterns = [
    # path('', views.BaseView.as_view(), name="base"),
    
    path('', views.IndexView.as_view(), name="index"),
    path('home-page.html', views.HomeView.as_view(), name="home-page"),
    path('services.html', views.ServicesView.as_view(), name="services"),
    path('about-us.html', views.AboutusView.as_view(), name="about-us"),
    path('about-me.html', views.AboutmeView.as_view(), name="about-me"),
    path('contacts.html', views.ContactsView.as_view(), name="contacts"),
    path('hm.html', views.HmView.as_view(), name="test"),
    # path('login.html', views.AcView.as_view(), name="accounts"),
    # path('create.html', views.AcView.as_view(), name="accounts"),
]
# urlpatterns = [
#     path('', include('django.contrib.auth.urls')),
# ]