from typing import Any, Dict
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.utils import timezone

from blog.models import Post

PER_PAGE = 9

def post_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_view.html', {'posts': posts})

