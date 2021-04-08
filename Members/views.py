from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import register_form
from .models import Member as member_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Api.backend import EmailOrUsernameModelBackend, Check_Account_member
from Home.models import Logo as logo_model

# Create your views here.
def get_page_register(request):
    logo = logo_model.objects.filter(status=True)[0]
    return render(request, 'pages/register.html',{'logo' : logo})

def get_page_login(request):
    logo = logo_model.objects.filter(status=True)[0]
    path = request.GET.get('path')
    return render(request, 'pages/sign_in.html', {'path' : path, 'logo' : logo})

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_name = request.POST['userName']
        password = request.POST['password']
        path = request.GET.get('path')
        if path == '' or path is not None:
            path = "/trangchu"   
        if not User.objects.filter(email= email).exists():
            if not User.objects.filter(username = user_name).exists():
                user = User(email = email, username = user_name, password = password)
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(path, {'user' : user})
            else:
                logo = logo_model.objects.filter(status=True)[0]
                return render(request, 'pages/register.html', {'message_user': 'tên người dùng đã tồn tại', 'logo' : logo})
        else:
            logo = logo_model.objects.filter(status=True)[0]
            return render(request, 'pages/register.html', {'message_email': 'email đã tồn tại', 'logo' : logo})
    else:
        return render(request, 'pages/error.html')
          

def login_user(request):
    account = request.POST['account']
    password = request.POST['password']
    #member = member_model.objects.filter(email = account, password = password, status = True)
    try:
        user = authenticate(request, username = User.objects.get(email = account), password = password)
    except:
        user = authenticate(request, username = account, password = password)
    #user = EmailOrUsernameModelBackend.authenticate(request, account, password)
    path = request.GET.get('path')
    if path == '' or path is not None:
        path = "/trangchu"
    if user is not None:
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(path ,{'user' : user})
    else:
        logo = logo_model.objects.filter(status=True)[0]
        return render(request, 'pages/sign_in.html', {'message': 'Tài khoản hoặc mật khẩu không đúng', 'logo' : logo})

def logout_user(request):
    logout(request)
    path = request.GET.get('path')
    return redirect(path)
