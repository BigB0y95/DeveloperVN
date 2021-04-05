from django.shortcuts import render
from django.http import request
from Home.models import Course as course_model

# Create your views here.
def get_post_by_id(request):
    course_list = course.objects.filter(status=True)
    return render(request, 'pages/Posts.html',{'course_list' : course_list})