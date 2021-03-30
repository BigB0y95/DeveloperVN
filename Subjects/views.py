from django.shortcuts import render
from django.http import HttpResponse
from .models import Subjects as subjects
from Lesson.models import Lesson as lesson

# Create your views here.
def get_page_subject(request, id):
    subject_list = subjects.objects.filter(course_id=id)
    message = ""
    lessons_list = list()
    if subject_list.count() != 0 :
        for subject in subject_list:
            lessons = lesson.objects.filter(subject_id = subject.subject_id)
            for ls in lessons:
                lessons_list.append(ls)
        return render(request, 'pages/subjects.html', {'title' : id, 'message' : message, 'subject_list' : subject_list, 'lessons_list' : lessons_list})       
    else:
        message = "Xin lỗi! Hiện chúng tối đang tiến hành cập nhật khóa học"
        return render(request, 'pages/subjects.html', {'title' : id, 'message' : message})
        
