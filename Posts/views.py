from django.shortcuts import render
from django.http import request
from django.db.models import F
from Home.models import Course as course_model, Logo as logo_model
from .models import Posts as posts_model

# Create get_post_by_id views.
def get_post_by_id(request, post_id, url_name):
    logo = logo_model.objects.filter(status=True)[0]
    # lấy danh sách khóa học
    course_list = course_model.objects.filter(status=True)   
    # tăng giá trị của trường views lên 1
    posts_model.objects.filter(post_id = post_id).update(views = F('views') + 1)
    # lấy bài viết theo mã
    post = posts_model.objects.get(post_id = post_id)
    # lấy 5 bai viết mới nhất
    post_list_new = posts_model.objects.extra(where=['post_id != %s'], params = [post_id]).order_by('createDate')[0:5]
    return render(request, 'pages/Posts.html',{'course_list' : course_list, 'post' : post, 'post_list_new' : post_list_new, 'logo':logo})