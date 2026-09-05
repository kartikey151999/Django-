from django.urls import path
from .views import about_django,about_fastapi,Home
urlpatterns = [
  path('',Home),
  path('django/',about_django),
  path('fastapi/',about_fastapi)
]