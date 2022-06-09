from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost


class BlogHomeView(ListView):
    """
    HomeView shows all the blog posts
    in reverse chronological order (newest first).
    Could also try to figure out how to implement
    sorting by most popular or implementing a search bar.
    """
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'
    paginate_by = 5

class BlogPostDetailView(DetailView):
    """
    Shows each individual blog post 
    and relevant information. 
    """
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'blog_post'
