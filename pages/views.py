from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Esto es lo nuevo:
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
