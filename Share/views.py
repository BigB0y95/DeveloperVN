from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Home.models import Course as course_model
from Posts.models import Posts as posts_model

# Create get page share views.
def get_page_share(request):
    # get list course with status is true
    course_list = course_model.objects.filter(status=True)
    # get list post with status is true
    post_list = posts_model.objects.filter(status=True)
    message = ''
    # if have not post
    if post_list.count() == 0:
        message = "Xin lỗi! Chúng tôi đang tiến hành cập nhật bài viết"
        print(message)
        return render(request, 'pages/Share.html',{'course_list' : course_list, 'post_list': post_list, 'message': message})
    # if post exist
    else:
        # thực hiện phân trang
        page = request.GET.get('page', 1)
        # chỉ định só phần tử trong 1 trang
        paginator = Paginator(post_list, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        print(message)
        return render(request, 'pages/Share.html',{'course_list' : course_list, 'post_list': post_list, 'message': message, 'posts':posts})