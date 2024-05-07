from typing import Any, Dict
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from blog.models import Page, Post

PER_PAGE = 9

class PostListView(ListView):
	template_name = 'blog/pages/index.html'
	context_object_name = 'posts'	
	paginate_by = PER_PAGE


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
	
		context.update({
				'page_title': 'Home - ',
		})
	
		return context

class PageDetailView(DetailView):
	model = Page
	template_name = 'blog/pages/page.html'
	slug_field = 'slug'
	context_object_name = 'page'

	def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
		ctx = super().get_context_data(**kwargs)
		page = self.get_object()
		page_title = f'{page.title} - Página - ' #type: ignore
		ctx.update({
			'page_title,'
		})
		return ctx
	
	def get_queryset(self) -> QuerySet[Any]:
		return super().get_queryset().filter(is_published=True)
	
class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/pages/post.html'
	context_object_name = 'post'

	def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
		ctx = super().get_context_data(**kwargs)
		post = self.get_object()
		page_title = f'{post.title} - Post - '
		ctx.update({
			'page_title': page_title,
		})
		return ctx
	
	def get_queryset(self) -> QuerySet[Any]:
		return super().get_queryset().filter(is_publishe=True)
	
