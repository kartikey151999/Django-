from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home1(request):
    return HttpResponse("Hello, welcome to the Home1 page!")

def About1(request):
    return HttpResponse("This is the About1 page.")
