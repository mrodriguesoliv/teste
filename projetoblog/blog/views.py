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
	
	
