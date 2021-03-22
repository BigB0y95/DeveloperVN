from django.urls import path
from .import views
from Home import views as home
from About import views as about
from Login import views as login
from Register import views as register
from Subjects import views as subjects
from Lesson import views as lesson

urlpatterns = {
    path('', views.index),
    path('trangchu', home.get_page_home),
    path('gioithieu', about.get_page_about),
    path('dangnhap', login.get_page_login),
    path('dangky', register.get_page_register),
    path('khoahoc', subjects.get_page_subject),
    path('baihoc', lesson.get_lesson_by_id)
}