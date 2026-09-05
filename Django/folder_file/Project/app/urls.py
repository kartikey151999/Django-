from . import views
from django.urls import path,re_path

urlpatterns=[
    path('<int:id>/',views.home,name='home'),
    path('<str:name>/',views.about,name='about'),
    re_path(r'^year/(?P<year>[0-9]{4})/$',views.year,name='year'),
    path('<int:day>/<int:month>/<int:year>/',views.year,name='year'),
]