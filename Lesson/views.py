from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from .models import Lesson as lesson_model
from Home.models import Course as course_model
from Subjects.models import Subjects as subject_model
from Sponsor.models import Info_Account as info_acc_module

# Create your views here.
def get_lesson_by_id(request, course_id, subject_id, lesson_id, url_name):
    # get course list
    course_list = course_model.objects.filter(status=True)
    # update subject with total visits + 1
    subject_model.objects.filter(subject_id= subject_id).update(totalVisits= F('totalVisits') + 1)
    # get subject by id
    subject = subject_model.objects.get(subject_id= subject_id)   
    # update lesson with views + 1
    lesson_model.objects.filter(lesson_id= lesson_id).update(views = F('views') + 1)
    # get lesson by id
    lesson = lesson_model.objects.get(lesson_id= lesson_id)
    # get lesson list by id of subject
    lesson_list = lesson_model.objects.filter(subject_id = subject_id)
    # get information account
    info_account_list = info_acc_module.objects.filter(status=True)
    id_next = lesson_id + 1
    id_prev = lesson_id - 1
    # get lesson next
    lessons_next = lesson_model.objects.filter(lesson_id = id_next, subject_id = subject_id)
    # get lesson prev
    lessons_prev = lesson_model.objects.filter(lesson_id = id_prev, subject_id = subject_id)
    # set disable for button next lesson
    if(len(lessons_next) > 0):
        lesson_next = lessons_next[0]
        disable_next = ""
        # set disable for button prev lesson
        if(len(lessons_prev) > 0):
            lesson_prev = lessons_prev[0]
            disable_prev = ""
            return render(request, 'pages/lesson.html', {'course_list' : course_list, 'subject' : subject,
            'lesson' : lesson, 'lesson_list' : lesson_list, 'disable_next': disable_next, 'disable_prev': disable_prev,
            'lesson_next': lesson_next, 'lesson_prev':lesson_prev, 'info_account_list': info_account_list})
        else:
            disable_prev = "disabled"
            return render(request, 'pages/lesson.html', {'course_list' : course_list, 'subject' : subject,
            'lesson' : lesson, 'lesson_list' : lesson_list, 'disable_next': disable_next, 'disable_prev': disable_prev,
            'lesson_next': lesson_next, 'info_account_list':info_account_list})
    else:
        disable_next = "disabled"
        # set disable for button prev lesson
        if(len(lessons_prev) > 0):
            lesson_prev = lessons_prev[0]
            disable_prev = ""
            return render(request, 'pages/lesson.html', {'course_list' : course_list, 'subject' : subject,
            'lesson' : lesson, 'lesson_list' : lesson_list, 'disable_next': disable_next, 'disable_prev': disable_prev,
            'lesson_prev':lesson_prev,'info_account_list':info_account_list})
        else:
            disable_prev = "disabled"
            return render(request, 'pages/lesson.html', {'course_list' : course_list, 'subject' : subject,
            'lesson' : lesson, 'lesson_list' : lesson_list, 'disable_next': disable_next,'info_account_list':info_account_list})