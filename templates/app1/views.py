from django.shortcuts import render
from datetime import datetime

# Create your views here.

def Home(request):
    return render(request, 'app1/home.html')

def About(request):
    dt = datetime.now()
    detail = {
        'name': 'Truth and Simplicity Org',
        'address': '123,Pavitra Puri, Anupshahr, Uttar Pradesh, India',
        'description': 'We are a non-profit organization dedicated to promoting truth and simplicity in our community.',
        'date': dt
        
    }
    return render(request, 'app1/about.html', detail)

def Services(request):
    # services = [
    #     {'name': 'Community Outreach', 'description': 'We organize events and programs to engage with the local community.'},
    #     {'name': 'Educational Workshops', 'description': 'We provide workshops on various topics related to truth and simplicity.'},
    #     {'name': 'Volunteer Opportunities', 'description': 'We offer opportunities for individuals to volunteer and contribute to our cause.'},
    # ]
    services = []
    return render(request, 'app1/services.html', {'services': services})