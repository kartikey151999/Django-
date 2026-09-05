from django.urls import path

from .views import PostDeleteView, PostDetailView, PostListView, PostUpdateView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='PostListView'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='PostDetailView'),
    path('create/', PostCreateView.as_view(), name='PostCreateView'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='PostUpdateView'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='PostDeleteView'),
]