from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'listview.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detailview.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'createview.html'
    fields = ['title', 'content']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'updateview.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'deleteview.html'
    success_url = reverse_lazy('PostListView')
