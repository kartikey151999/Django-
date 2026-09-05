from django.urls import path
from .views import Learn_django
urlpatterns=[
    path('django/',Learn_django)
]