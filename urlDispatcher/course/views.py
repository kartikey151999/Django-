from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Python(request,**Course):
    course = Course.get("course","no course available") 
    return HttpResponse(f"{course}")


def Django(request,**Course):
    course = Course.get("course","no course available") 
    return HttpResponse(f"{course} ")


def flask(request,**Course):
    course = Course.get("course","no course available") 
    return HttpResponse(f"{course}")