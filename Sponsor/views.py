from django.shortcuts import render
from Home.models import Course as course_model 
from .models import Info_Account as info_acc_model, Sponsor as sponsor_model

# Create your views here.
def get_page_sponsor(request):
    # get course list
    course_list = course_model.objects.all()
    info_account_list = info_acc_model.objects.filter(status = True)
    sponsor_list = sponsor_model.objects.select_related('account_id')
    return render(request, 'pages/sponsor.html', {'course_list': course_list, 'info_account_list' : info_account_list, 'sponsor_list' : sponsor_list})
