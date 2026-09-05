from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name='blog'), 
    path('base', views.base, name='base'), 
]

