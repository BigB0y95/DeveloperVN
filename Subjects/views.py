from django.shortcuts import render
from django.http import HttpResponse
from .models import Subjects as subjects

# Create your views here.
def get_page_subject(request):
    subjectList = subjects.objects.all()
    return render(request, 'pages/subjects.html', {'subjectList' : subjectList})
