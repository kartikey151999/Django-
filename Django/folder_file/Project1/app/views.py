from django.shortcuts import render

from datetime import datetime

# Create your views here.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def home(request):
    content={
        'name': 'Kartikey',
        'age': 20,
        'date': datetime.now(),
        'user': User('Kartikey Pande', 27),
        'address':{
            'city': 'Anupshahr',
            'state': 'Uttar Pradesh',
            'country': 'India'
        },
        'fruits': ['<b>Apple</b>', '<i>Banana</i>', '<u>Mango</u>', '<s>Grapes</s>'],
        'empty_list': None  
    }     


    return render(request, 'home.html', content)   