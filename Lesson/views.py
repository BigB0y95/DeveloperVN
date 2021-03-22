from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_lesson_by_id(request):
    return render(request, 'pages/lesson.html')