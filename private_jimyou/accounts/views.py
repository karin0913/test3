from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Usertest
from django.views.generic import CreateView,TemplateView,UpdateView
from jimyou.forms import UserCreateForm, LoginForm, UserUpdateForm,ProfileCreateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout


from datetime import datetime
from datetime import datetime,timedelta
def index(request):
  template_name = "login_app/index.html" # templates以下のパスを書く
  birthday = Usertest.objects.all().values("birthday")
  test = '2002-01-01'
# 171.55 2083344+172limitdata = 81.47  
#   birthday = birthday + datetime.timedelta(years=+81,months=+5,days=+22)
  ctx = {"birthday": birthday,}
  return render(request,template_name,ctx)

def main_page(request):
    return render(request, 'registration/login.html')

def new_login_page(request):
    return render(request, 'registration/create.html')

def logout_page(request):
    return render(request, 'registration/logout.html')

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "login_app/index.html"


#アカウント作成
class Create_Account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            #フォームに入力された'username', 'password1'が一致する会員をDBから探し，userに代入
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/create.html', {'form': form,})
    def get(self, request, *args, **kwargs):
        checks_value = request.POST.getlist('checks[]')

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'registration/create.html', {'form': form,})

create_account = Create_Account.as_view()

#ログイン
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = Usertest.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'registration/login.html', {'form': form,})

account_login = Account_login.as_view()

#ユーザー情報更新
class UserUpdateForm(UpdateView):
    model = Usertest
    form_class = UserUpdateForm
    template_name = 'registration/user_form.html'

from datetime import datetime
import django.utils.timezone
class ProfileForm(UpdateView):
    model = Usertest
    # def get_birthday(self, request, *args, **kwargs):
    #     # form = ProfileCreateForm(data=request.POST)
    #     # birthday = Usertest.objects.all().values("birthday")
    #     # date_format = "%Y-%m-%d"
    #     # test = datetime.strptime(birthday, date_format)
    #     # # 171.55 2083344+172
    #     # limitdata = 81.47  
    #     # test = test + limitdata
    #     test = '2002-01-01'
    #     ctx = {"birthday": test,}
    #     return render(request, 'registration/profilecreate.html',ctx)

    def post(self, request, *args, **kwargs):
        form = ProfileCreateForm(data=request.POST)
        return render(request, 'registration/profilecreate.html', {'form': form,})
    def get(self, request, *args, **kwargs):
        checks_value = request.POST.getlist('checks[]')

    def get(self, request, *args, **kwargs):
        form = ProfileCreateForm(request.POST)
        return  render(request, 'registration/profilecreate.html', {'form': form,})


# return render(request, 'mutual/index.html',{'propertys': propertys})
# https://qiita.com/knakajima3027/items/34b2a105da7cdb411736
# https://teratail.com/questions/270692