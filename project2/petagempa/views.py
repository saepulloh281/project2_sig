from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html')

def berita(request):
    return render (request, 'berita.html')
# Create your views here.
