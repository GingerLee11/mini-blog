from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.http import Http404, HttpResponseForbidden

from .models import BlogPost, Comment

from users.models import BlogUser
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentFormView(SingleObjectMixin, FormView):
    """
    View for the comment form, which allows users to 
    leave comments user a blog post if logged in.
    """
    template_name = 'blog/blogpost_detail.html'
    form_class = CommentForm
    model = Comment
    success_url = '#'

    def post(self, request, *args, **kwargs):
        """
        Posts the comment only if the user is logged in.
        """
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    
class PostView(View):

    def get(self, request, *args, **kwargs):
        view = BlogPostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        form = CommentForm(request.POST)
        # Set the current user
        # to the comment_author field
        form.instance.comment_author = request.user
        # Set the blog post as the current blogpost
        form.instance.post = BlogPost.objects.get(id=self.kwargs['pk'])
        if form.is_valid():
            form.save()
        return view(request, *args, **kwargs)


class UserDetailView(DetailView):
    """
    Detailed view of the author on the blog.
    """
    model = BlogUser
    template_name = 'blog/author_detail.html'
    context_object_name = 'bloguser'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_queryset(self):
        return super().get_queryset().filter(username=self.kwargs['username'])

    def get_object(self, queryset=None):
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView

        # Define the slug
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by slug.
        elif slug is not None:


            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj
    

'''
class UserListView(ListView):
    """
    List view of all the authors on the blog.
    """
    model = BlogUser
    template_name = 'blog/author_list.html'
    context_object_name = 'blogusers'
'''