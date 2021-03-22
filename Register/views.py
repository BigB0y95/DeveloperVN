from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_page_register(request):
    return render(request, 'pages/register.html')