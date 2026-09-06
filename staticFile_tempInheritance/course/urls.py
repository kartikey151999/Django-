from django.urls import path
from .views import about_django,about_fastapi,Home
urlpatterns = [
  path('',Home,name='home'),
  path('django/',about_django,name='course'),
  path('fastapi/',about_fastapi,name='course')
]