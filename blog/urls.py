from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='index'),
    path('blog/<int:pk>/', views.PostView.as_view(), name='blog-detail'),
    path('bloguser/<slug:username>/', views.UserDetailView.as_view(), name='bloguser-detail'),
    # path('blogusers/', views.UserListView.as_view(), name='bloguser-list'),
]