from django.urls import path
from blog.views import (post_view)


app_name = 'blog'

urlpatterns = [
    path('', post_view.as_view, name='post_view'),
]

