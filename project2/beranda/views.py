from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("SELAMAT DATANG DI HALAMAN BERANDA!!")

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')
    