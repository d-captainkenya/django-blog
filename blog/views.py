from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    #context_object_name = 'all_posts_list'                 raising reverse error
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    #context_object_name = 'indiv_post'                     raising reverse error
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')