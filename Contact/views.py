from django.shortcuts import render, redirect
from django.http import HttpResponse
from Home.models import Course as course_model
from .models import Contact_User as contact_user, Contact_Live as contact_live

# Create your views here.
def get_page_contact(request):
    course_list = course_model.objects.filter(status=True)
    contact_live_list = contact_live.objects.filter(status=True)
    message = request.GET.get("thongbao")
    return render(request, 'pages/contact.html', {'course_list' : course_list,'contact_live_list' : contact_live_list, 'message':message})

def send_contact(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]

        contact = contact_user(contact_person = fullname, mail = email, phone = phone, content= content)
        contact.save()
        path = request.GET.get("path")

        return redirect(path + '?thongbao=true')
    else :
        return render(request, 'pages/error.html')