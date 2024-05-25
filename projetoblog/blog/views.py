from typing import Any, Dict
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404

PER_PAGE = 9

def post_view(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_view.html', {'posts': posts})


def testess(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/testess.html', {'post': post})