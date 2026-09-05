from django.shortcuts import render

# Create your views here.
def django_fees(request):
    return render(request,'course_fees/django_fees.html')


def fastapi_fees(request):
    return render(request,'course_fees/fastapi_fees.html')