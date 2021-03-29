from django.urls import path
from .import views
from Home import views as home
from About import views as about
from Subjects import views as subjects
from Lesson import views as lesson
from Members import views as member

urlpatterns = [
    path('', views.index),
    path('trangchu', home.get_page_home),
    path('gioithieu', about.get_page_about),
    path('dangnhap', member.get_page_login),
    path('dangky', member.get_page_register),
    path('dangkythanhvien', member.register),
    path('dangnhaptaikhoan', member.login_user),
    path('dangxuat', member.logout_user),
    path('khoahoc/<str:id>/', subjects.get_page_subject),
    path('baihoc', lesson.get_lesson_by_id)
]