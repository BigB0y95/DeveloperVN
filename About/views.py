from django.shortcuts import render
from django.http import HttpResponse
from .models import About as about_model
# Create your views here.
def get_page_about(request):
    about = about_model.objects.get(status=True)
    return render(request, 'pages/about.html', {'about' : about})