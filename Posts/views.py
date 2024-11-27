from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost

class BlogView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = "Posts/blogView.html"

class BlogCreate(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'author']
    template_name = "Posts/blogcreate.html"
    success_url = reverse_lazy('Posts:listhtml')

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author', 'content']
    pk_url_kwarg = 'pk'
    template_name = "Posts/blogUpdate.html"
    success_url = reverse_lazy('Posts:listhtml')

class BlogDeleteView(DeleteView):
    model = BlogPost
    pk_url_kwarg = 'pk'
    template_name = "Posts/blogdelete.html"
    success_url = reverse_lazy('Posts:listhtml')
