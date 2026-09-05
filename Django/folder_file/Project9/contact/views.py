from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def contact_form(request):
    return render(request,'contact.html')


def submit(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        print(name,email)
        if name and email:
            Contact.objects.create(name = name , email = email)
            return HttpResponse("successfully posted")
        else:
            return HttpResponse("missing data")
        

    return redirect(contact_form)