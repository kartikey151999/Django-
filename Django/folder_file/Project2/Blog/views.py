from django.shortcuts import render
# Create your views here.

def home(request):  
    return render(request, 'Home.html')

def blog(request):
    return render(request, 'Blog.html')