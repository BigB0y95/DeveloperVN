from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Course as course
# Create your views here.
def index(request):
    course_list = course.objects.all()
    return render(request, 'pages/home.html', {'course_list' : course_list})

