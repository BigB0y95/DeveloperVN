from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Course as course_model, Logo as logo_model, Banner as banner_model
# Create your views here.
def index(request):
    course_list = course_model.objects.filter(status=True)
    logo = logo_model.objects.filter(status=True)[0]
    banner_list = banner_model.objects.filter(status=True).order_by('priority')[0:3]
    return render(request, 'pages/home.html', {'course_list' : course_list, 'logo': logo, 'banner_list':banner_list})

