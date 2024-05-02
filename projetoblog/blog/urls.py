from blog.views import (PostListView, PageDetailView, PostDetailView)
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/', PostDetailView.as_view(), name='post')
    ]