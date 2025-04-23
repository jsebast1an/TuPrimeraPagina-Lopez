from django.shortcuts import render
from django.http import HttpResponse
from django.urls import include

def index(request):
    return render(request, 'index.html')
