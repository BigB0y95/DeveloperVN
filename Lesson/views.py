from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson as lesson_model

# Create your views here.
def get_lesson_by_id(request, course_id, subject_id, lesson_id, url_name):
    lesson = lesson_model.objects.get(lesson_id= lesson_id)
    return render(request, 'pages/lesson.html', {'lesson' : lesson})