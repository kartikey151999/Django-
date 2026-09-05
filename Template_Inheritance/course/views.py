from django.shortcuts import render

# Create your views here.
def about_django(request):
    return render(request,'course/course.html',{'course':'django'})

def about_fastapi(request):
    return render(request,'course/course.html',{'course':'fastapi'})

def Home(request):
    return render(request,'course/Base.html')
