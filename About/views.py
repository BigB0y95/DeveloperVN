from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_page_about(request):
    return render(request, 'pages/about.html')