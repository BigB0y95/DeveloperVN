from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Home.models import Course as course_model 
from .models import Info_Account as info_acc_model, Sponsor as sponsor_model

# Create your views here.
def get_page_sponsor(request):
    # get course list
    course_list = course_model.objects.filter(status=True)
    info_account_list = info_acc_model.objects.filter(status = True)
    sponsor_list = sponsor_model.objects.all().select_related('account').order_by('sponsor_id')

    page = request.GET.get('page', 1)
    paginator = Paginator(sponsor_list, 8)
    try:
        sponsor = paginator.page(page)
    except PageNotAnInteger:
        sponsor = paginator.page(1)
    except EmptyPage:
        sponsor = paginator.page(paginator.num_pages)
    
    return render(request, 'pages/sponsor.html', {'course_list': course_list, 'info_account_list' : info_account_list, 'sponsor_list' : sponsor})
