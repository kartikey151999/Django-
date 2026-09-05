from django.urls import path
from .views import django_fees,fastapi_fees
urlpatterns=[
  path('django/',django_fees),
  path('fastapi/',fastapi_fees)

]