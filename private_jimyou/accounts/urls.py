from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth.views import login, logout

urlpatterns = [
    path('templates/login_app/index.html',  views.View.as_view(), name='index'),
    path('templates/registration/create.html',  views.View.as_view(), name='create'),
    path('', include('django.contrib.auth.urls')),
    # path('home-page.html', views.HomeView.as_view(), name="home-page"),
]


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', views.index, name='index'),
#     url(r'^create/$', views.create_account, name='create_account'),
#     url(r'^login/$', views.account_login, name='login'),
#     url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),
# ]