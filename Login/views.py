from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_page_login (request):
    return render(request, 'pages/sign_in.html')