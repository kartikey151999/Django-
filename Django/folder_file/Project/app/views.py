from django.http import HttpResponse

# Create your views here.
def home(request, id):  
    return HttpResponse(f"Hello, World! ID: {id}")

def about(request, name):
    return HttpResponse(f"Hello, {name}!")


def year(request, **kwargs):
    return HttpResponse(f"Date :{kwargs['day']}/{kwargs['month']}/{kwargs['year']}")