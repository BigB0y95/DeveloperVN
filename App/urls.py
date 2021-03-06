from django.urls import path
from .import views
from Home import views as home
from About import views as about
from Subjects import views as subjects
from Lesson import views as lesson
from Members import views as member
from Contact import views as contact
from Sponsor import views as sponsor
from Share import views as share
from Posts import views as posts

urlpatterns = [
    path('', views.index),
    path('trangchu', home.get_page_home),
    path('gioithieu', about.get_page_about),
    path('dangnhap', member.get_page_login),
    path('dangky', member.get_page_register),
    path('dangkythanhvien', member.register),
    path('dangnhaptaikhoan', member.login_user),
    path('doimatkhau', member.get_page_change_pass),
    path('thaydoimatkhau', member.change_pass),
    path('dangxuat', member.logout_user),
    path('laylaimatkhau', member.get_page_pass_retrieval),
    path('guima', member.sent_code),
    path('khoahoc/<str:id>/', subjects.get_page_subject),
    path('khoahoc/<str:course_id>/<str:subject_id>/<int:lesson_id>/<str:url_name>/', lesson.get_lesson_by_id),
    path('lienhe', contact.get_page_contact),
    path('guilienhe', contact.send_contact),
    path('taitro', sponsor.get_page_sponsor),
    path('chiase', share.get_page_share),
    path('chiase/<int:post_id>/<str:url_name>', posts.get_post_by_id)
]