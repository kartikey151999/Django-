"""
URL configuration for functionalView project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as ap1_views
from app2 import views as ap2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ap1_views.Home, name='home'),  
    path('Home/', ap1_views.Home, name='home'),
    path('About/', ap1_views.About, name='about'),
    path('Home1/', ap2_views.Home1, name='home1'),
    path('About1/', ap2_views.About1, name='about1'),
]
