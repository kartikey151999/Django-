from django.shortcuts import render



def Learn_django(request):
    return render(request,'Course/learn_django.html',{'version':'3.2.6'})

# Create your views here.
