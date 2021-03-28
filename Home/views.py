from django.shortcuts import render
from django.http import HttpResponse
from Subjects.models import Subjects as subjects
# Create your views here.
def get_page_home(request):
    subjectList = subjects.objects.all()
    return render(request, 'pages/home.html', {'subjectList' : subjectList})
