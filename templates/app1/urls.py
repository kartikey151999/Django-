from django.urls import path

from .views import About, Home, Services

urlpatterns = [ 
    path('home/', Home, name='home'),
    path('about/', About, name='about'),
    path('services/', Services, name='services')
]  