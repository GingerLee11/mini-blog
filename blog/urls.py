from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='index'),
    path('blog/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
]