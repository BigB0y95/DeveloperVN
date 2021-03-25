from django.shortcuts import render
from django.http import HttpResponse
from .forms import register_form
from .models import Member as member_model

# Create your views here.
def get_page_register(request):
    return render(request, 'pages/register.html')

def get_page_login(request):
    return render(request, 'pages/sign_in.html')

def register(request):
    if request.method == "POST":
        rf = register_form(request.POST)
        if rf.is_valid():
            save_rf = member_model(email = rf.cleaned_data["email"], password = rf.cleaned_data["password"], status = True)
            save_rf.save()
            return render(request, 'pages/sign_in.html')
        else:
            return render(request, 'pages/error.html')
    else:
        return render(request, 'pages/error.html')
