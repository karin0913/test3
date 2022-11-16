from django.shortcuts import render
from django.views import generic

class BaseView(generic.TemplateView):
    template_name = "base.html"

class IndexView(generic.TemplateView):
    template_name = "index.html"

class HomeView(generic.TemplateView):
    template_name = "home-page.html"

class ServicesView(generic.TemplateView):
    template_name = "services.html"

class AboutusView(generic.TemplateView):
    template_name = "about-us.html"

class AboutmeView(generic.TemplateView):
    template_name = "about-me.html"

class ContactsView(generic.TemplateView):
    template_name = "contacts.html"

class HmView(generic.TemplateView):
    template_name = "hm.html"

class GurafuView(generic.TemplateView):
    template_name = "gurafu.html"

from django.contrib.auth.decorators import login_required
class AcView(generic.TemplateView):
    @login_required
    def index(request):
        return render(request, 'login_app/index.html')
