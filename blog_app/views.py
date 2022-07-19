from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin 

class index(ListView):                          # index View
    model=Post
    template_name='index.html'

class blogs(DetailView):                        # blog view
    model=Post
    template_name='blogs.html'



class add_post( LoginRequiredMixin, CreateView):   # Add Post View
    model=Post
    template_name='add_post.html'
    fields='__all__'



class update_post( LoginRequiredMixin, UpdateView): # Edit Post view
    model=Post
    template_name='update_post.html'
    fields=['title','body']


class delete_post( LoginRequiredMixin, DeleteView): # Delete Post view
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('index')