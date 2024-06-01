from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_view, name='post_view'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]

