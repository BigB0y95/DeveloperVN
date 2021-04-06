from django.shortcuts import render
from django.http import HttpResponse
from .models import Course as course_model, Logo as logo_model
# Create your views here.
def get_page_home(request):
    course_list = course_model.objects.filter(status=True)
    logo = logo_model.objects.filter(status=True)[0]
    return render(request, 'pages/home.html', {'course_list' : course_list, 'logo': logo})
