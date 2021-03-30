from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson as lesson_model
from Home.models import Course as course_model
from Subjects.models import Subjects as subject_model

# Create your views here.
def get_lesson_by_id(request, course_id, subject_id, lesson_id, url_name):
    course_list = course_model.objects.all()
    subject = subject_model.objects.get(subject_id= subject_id)
    lesson = lesson_model.objects.get(lesson_id= lesson_id)
    lesson_list = lesson_model.objects.filter(subject_id = subject_id)
    return render(request, 'pages/lesson.html', {'course_list' : course_list, 'subject' : subject, 'lesson' : lesson, 'lesson_list' : lesson_list})