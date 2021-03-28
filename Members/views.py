from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import register_form
from .models import Member as member_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def get_page_register(request):
    return render(request, 'pages/register.html')

def get_page_login(request):
    return render(request, 'pages/sign_in.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_name = request.POST['userName']
        password = request.POST['password']       
        if not member_model.objects.filter(email= email).exists():
            member = member_model(email = email, userName = user_name, password = password, status= True)
            member.save()
            return redirect('/dangnhap')
        else:
            return render(request, 'pages/register.html', {'message_email': 'email đã tồn tại'})
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
    if user is not None:
        login(request, user)
        return redirect('/trangchu' ,{'user' : user})
    else:
        return redirect('/dangnhap', {'message': 'Tài khoản hoặc mật khẩu không đúng'})

def logout_user(request):
    logout(request)
    url_present = request.path
    return redirect(url_present)
