from django.shortcuts import render
from .models import Student
# Create your views here.
def app(request):
    students = Student.objects.all()
    return render(request,'App.html',{'students':students})