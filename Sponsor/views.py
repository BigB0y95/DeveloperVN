from django.shortcuts import render
from Home.models import Course as course_model

# Create your views here.
def get_page_sponsor(request):
    course_list = course_model.objects.all()
    return render(request, 'pages/sponsor.html', {'course_list' : course_list})
