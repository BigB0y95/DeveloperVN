from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import register_form
from .models import Member as member_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Api.backend import EmailOrUsernameModelBackend, Check_Account_member
from Home.models import Logo as logo_model
from django.core.mail import send_mail
import random

# Create your views here.
def get_page_register(request):
    logo = logo_model.objects.filter(status=True)[0]
    path = request.GET.get('path')
    return render(request, 'pages/register.html',{'path' : path, 'logo' : logo})

def get_page_login(request):
    logo = logo_model.objects.filter(status=True)[0]
    path = request.GET.get('path')
    return render(request, 'pages/sign_in.html', {'path' : path, 'logo' : logo})

def get_page_change_pass(request):
    logo = logo_model.objects.filter(status=True)[0]
    path = request.GET.get('path')
    return render(request, 'pages/change_pass.html', {'path' : path, 'logo' : logo})

def get_page_pass_retrieval(request):
    logo = logo_model.objects.filter(status=True)[0]
    path = request.GET.get('path')
    return render(request, 'pages/password_retrieval.html', {'path' : path, 'logo' : logo})


def register(request):
    if request.method == 'POST':
        # lấy email mà người dùng nhập vào
        email = request.POST['email']
        # lấy tên người dùng mà người dùng nhập vào
        user_name = request.POST['userName']
        # lấy mật khẩu mà người dùng nhập vào
        password = request.POST['password']
        # lấy đường dẫn
        path = request.GET.get('path')
        # trường hợp path rỗng thì trả về trang chủ
        if path == '':
            path = "/trangchu"
        # kiểm tra xem email đã tồn tại hay chưa
        if not User.objects.filter(email= email).exists():
            # kiểm tra xem tên người dùng đã tồn tại hay chưa
            if not User.objects.filter(username = user_name).exists():
                # tạo người dùng mới với email và username mà người dùng nhập vào
                user = User.objects.create(email = email, username = user_name)
                # tạo password 
                user.set_password(password)
                # lưu người dùng
                user.save()
                user_login = authenticate(request, username = user_name, password = password)
                login(request, user_login, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(path, {'user' : user_login})
            else:
                logo = logo_model.objects.filter(status=True)[0]
                return render(request, 'pages/register.html', {'message_user': 'tên người dùng đã tồn tại', 'logo' : logo})
        else:
            logo = logo_model.objects.filter(status=True)[0]
            return render(request, 'pages/register.html', {'message_email': 'email đã tồn tại', 'logo' : logo})
    else:
        return render(request, 'pages/error.html')

def login_user(request):
    # lấy tài khoản mà người dùng nhập vào
    account = request.POST['account']
    # lấy mật khẩu mà người dùng nhập vào
    password = request.POST['password']
    try:
        # kiểm tra thông tin tài khoản với email và password
        user = authenticate(request, username = User.objects.get(email = account), password = password)
    except:
        # kiểm tra thông tin tài khoản với tên người dùng và password
        user = authenticate(request, username = account, password = password)
    #user = EmailOrUsernameModelBackend.authenticate(request, account, password)
    path = request.GET.get('path')
    if path == '':
        path = "/trangchu"
    # trường hợp tài khoản tồn tại
    if user is not None:
        # đăng nhập với tài khoản người dùng nhập vào
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(path, {'user' : user})
    # trường hợp tài khoản không tồn tại
    else:
        logo = logo_model.objects.filter(status=True)[0]
        return render(request, 'pages/sign_in.html', {'message': 'Tài khoản hoặc mật khẩu không đúng', 'logo' : logo, 'path' : path})

def logout_user(request):
    logout(request)
    path = request.GET.get('path')
    return redirect(path)

def change_pass(request):
    if request.method == 'POST':
        path = request.GET.get('path')
        if path == '':
            path = "/trangchu"
        # lấy mật khẩu hiện tại mà người dùng nhập vào
        current_pass = request.POST['currentPassword']
        # lấy mật khẩu mới mà người dùng nhập vào
        new_pass = request.POST['newPassword']
        # kiểm tra người dùng đã đăng nhập hay chưa
        if request.user.is_authenticated:
            # lấy tên người dùng từ tài khoản đang đăng nhập
            user_name = request.user.username
            # kiểm tra người dùng có tồn tại hay không
            user = authenticate(request, username = user_name, password = current_pass)
            # nếu người dùng tồn tại
            if user is not None:
                # thay đổi mật khẩu bằng mật khấu mới mà người dùng nhập vào
                user.set_password(new_pass)
                # lưu thông tin người dùng
                user.save()
                # kiểm tra
                user_login = authenticate(request, username = user_name, password = new_pass)
                login(request, user_login, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(path, {'user' : user_login})
            else:
                logo = logo_model.objects.filter(status=True)[0]
                # trả về trang change_pass.html và gửi thông báo cho người dùng
                return render(request, 'pages/change_pass.html', {'path' : path, 'logo' : logo,'message':'Mật khẩu hiện tại không đúng'})
        else:
            return render(request, 'pages/error.html')
    else:
        return render(request, 'pages/error.html')

def sent_code(request):
    if request.method == 'POST':
        path = request.GET.get('path')
        email = request.POST['email']
        message = ''
        if User.objects.filter(email=email).exists():
            code_number = random.randint(100000, 999999)
            #try:
            send_mail(
                'Lấy lại mật khẩu',
                'Mã xác minh để lấy lại mật khẩu của bạn là: ' + str(code_number),
                'quangpc.developervietnam@gmail.com',
                [email],
                fail_silently=False
            )
            logo = logo_model.objects.filter(status=True)[0]
            return render(request, 'pages/check_code.html', {'path' : path, 'logo' : logo})
            #except:
                #return render(request, 'pages/error.html')
        else:
            logo = logo_model.objects.filter(status=True)[0]
            message = 'Email chưa đăng ký tài khoản'
            return render(request, 'pages/password_retrieval.html', {'path' : path, 'logo' : logo,'message': message})
    else:
        return render(request, 'pages/error.html')

