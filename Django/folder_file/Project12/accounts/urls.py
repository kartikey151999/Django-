from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('view', views.view, name='view'), 
]