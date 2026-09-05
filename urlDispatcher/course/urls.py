from django.urls import path

from .views import Python, Django, flask

urlpatterns = [
    path('python/', Python,{'course':'Python'}),
    path('django/', Django,{'course':'Django'}),
    path('flask/', flask),
]