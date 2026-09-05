from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog.html')

def base(request):
    return render(request, 'base.html')