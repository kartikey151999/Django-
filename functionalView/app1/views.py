from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return HttpResponse("Hello, welcome to the Home page!")

def About(request):
    return HttpResponse("This is the About page.")
