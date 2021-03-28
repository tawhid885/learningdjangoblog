from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostcreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name = 'blog-home'),
    path('post/new/',PostcreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name = 'post-delete'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('about/',views.about, name = 'blog-about'),
    
]
