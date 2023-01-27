from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from jimyou.models import Profiletest,Usertest,Profilet
from jimyou.forms import CreateForm
import datetime
class BaseView(generic.TemplateView):
    template_name = "base.html"
    
    


class IndexView(generic.TemplateView):
    template_name = "index.html"
    def birthday(request,year, month, day):
        Birthday = Usertest.objects.get(test='birthday')
        today = datetime.date.today()
        birthday = datetime.date(Usertest.objects.get(test='birthday'))
        context = {'Birthday':Birthday, }
        return (int(today.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000

class HomeView(generic.TemplateView):
    template_name = "home-page.html"

class AboutusView(generic.TemplateView):
    template_name = "about-us.html"

class AboutmeView(generic.TemplateView):
    template_name = "about-me.html"

class ContactsView(generic.TemplateView):
    template_name = "contacts.html"

def add(request):
    """
    日記の記事を追加
    """
    # 送信内容を元にフォームを作る。POSTじゃなければ空のフォームを作成。
    form = CreateForm(request.POST or None)

    # method==POSTとは送信ボタンが押されたとき。form.is_validは入力内容に問題が無い場合Trueになる。
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('../../')

    # 通常時のアクセスや入力内容に誤りがあれば、再度day_form.htmlを表示
    context = {
        'form':form
    }
    return render(request, 'contacts.html', context)

class HmView(generic.TemplateView):
    template_name = "hm.html"

class GurafuView(generic.TemplateView):
    template_name = "gurafu.html"

from .forms import CreateForm
def home_view(request):
    context = {}
    context['form'] = CreateForm()
    return render(request, 'index.html', context)



def profile(request):
    """
    日記の一覧
    """
    context = {
        'profile_list':Profilet.objects.all(),
    }
    return render(request, 'services.html', context)

from django.views import View
from jimyou.forms import LoginForm
from django.contrib.auth import login
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = Usertest.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'index-account.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'index-account.html', {'form': form,})

