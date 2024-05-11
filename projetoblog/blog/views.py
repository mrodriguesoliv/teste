from typing import Any, Dict
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import Page, Post

PER_PAGE = 9

class Teste(ListView):
    def index(request):
        return render(request, 'teste.html')

