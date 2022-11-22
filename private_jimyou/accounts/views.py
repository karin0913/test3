from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import CustomUser
from django.views.generic import CreateView,TemplateView,UpdateView
from . forms import UserCreateForm, LoginForm, UserUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout


def index(request):
  template_name = "login_app/index.html" # templates以下のパスを書く
  return render(request,template_name)

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
        form = UserCreateForm(request.POST)
        return  render(request, 'registration/create.html', {'form': form,})

create_account = Create_Account.as_view()

#ログイン
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = CustomUser.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'registration/login.html', {'form': form,})

account_login = Account_login.as_view()

#ユーザー情報更新
class UserUpdateForm(UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'registration/user_form.html'




# https://qiita.com/knakajima3027/items/34b2a105da7cdb411736
# https://teratail.com/questions/270692
