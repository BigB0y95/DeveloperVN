from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Course as course_model

# Create your views here.
def get_page_contact(request):
    course_list = course_model.objects.all()
    return render(request, 'pages/contact.html', {'course_list' : course_list})