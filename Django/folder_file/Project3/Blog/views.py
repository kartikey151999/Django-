from django.shortcuts import render

# Create your views here.
def blog(request):
    students=[
        {'name':'Alice','age':20},          
        {'name':'Bob','age':22},
        {'name':'Charlie','age':21},    
    ]   
    return render(request,'blog.html',{'students':students})


def about(request):
    return render(request,'about.html')