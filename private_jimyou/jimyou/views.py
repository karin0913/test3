from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from jimyou.models import Profiletest,Usertest

class BaseView(generic.TemplateView):
    template_name = "base.html"

class IndexView(generic.TemplateView):
    template_name = "index.html"

class HomeView(generic.TemplateView):
    template_name = "home-page.html"

class ServicesView(generic.TemplateView):
    template_name = "services.html"
    def indexprofile(request):
        """
        日記の一覧
        """
        context = {
            'profile_list':Profiletest.objects.all(),
        }
        return render(request, 'services.html', context)
    def test(request):
        return Usertest.objects.all()
    def index(request):
        user = request.user


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

def indexprofile(request):
    """
    日記の一覧
    """
    context = {
        'profile_list':Profiletest.objects.all(),
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






# fields = ('user', 'limit', 'title', 'text')

# from .models import Profiletest
# from django.http import HttpResponse
# def create_view(request):
#     form = CreateForm(request.POST)
#     if not form.is_valid():
#         return HttpResponse('invalid', status=500)

#     user = form.cleaned_data['user']
#     limit = form.cleaned_data['limit']
#     title = form.cleaned_data['title']
#     text = form.cleaned_data['text']

#     post = Profiletest.objects.create(user=user, limit=limit,title=title, text=text)

#     return HttpResponse(f'{post.id}')









# from django.contrib.auth.decorators import login_required
# class AcView(generic.TemplateView):
#     @login_required
#     def index(request):
#         return render(request, 'login_app/index.html')

# from django.shortcuts import render, redirect
# from django.views import View
# from django.views import generic
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
# from django.views.generic import CreateView, TemplateView


# class ACindexView(generic.TemplateView):
#     template_name = "login_app/index.html"
# class ACView(generic.TemplateView):
#     template_name = "registration/create.html"

# def top_page(request):
#     return render(request, 'users_management_app/top_page.html')

# def main_page(request):
#     return render(request, 'login_app/index.html')

# def new_login_page(request):
#     return render(request, 'registration/create.html')



# #アカウント作成
# class Create_Account(CreateView):
#     def post(self, request, *args, **kwargs):
#         form = UserCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             #フォームから'username'を読み取る
#             username = form.cleaned_data.get('username')
#             #フォームから'password1'を読み取る
#             password = form.cleaned_data.get('password1')
#             #フォームに入力された'username', 'password1'が一致する会員をDBから探し，userに代入
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         return render(request, 'create.html', {'form': form,})

#     def get(self, request, *args, **kwargs):
#         form = UserCreateForm(request.POST)
#         return  render(request, 'create.html', {'form': form,})

# create_account = Create_Account.as_view()

# #ログイン
# class Account_login(View):
#     def post(self, request, *arg, **kwargs):
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             user = User.objects.get(username=username)
#             login(request, user)
#             return redirect('/')
#         return render(request, 'login.html', {'form': form,})

#     def get(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         return render(request, 'login.html', {'form': form,})

# account_login = Account_login.as_view()
