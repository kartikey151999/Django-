from django.urls import path
from . import views
urlpatterns = [
   path('',views.show_task,name='show_task'),
   path('add/',views.add_task,name='add_task'),
   path('edit/<int:tk>',views.edit_task,name='edit_task'),
   path('delete/<int:tk>',views.delete_task,name='delete_task'),
   path('toggle/<int:tk>',views.toggle_task,name='toggle_task'),
]