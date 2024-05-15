from django.urls import path
from blog.views import (post_view)
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_view, name='post_view'),
]
