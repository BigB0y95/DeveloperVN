from django.shortcuts import render
from django.http import HttpResponse
from .models import About as about_model
from Home.models import Course as course_model
# Create your views here.
def get_page_about(request):
    course_list = course_model.objects.filter(status=True)
    about = about_model.objects.get(status=True)
    return render(request, 'pages/about.html', {'about' : about, 'course_list': course_list})