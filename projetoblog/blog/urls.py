from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import include

app_name = 'blog'

urlpatterns = [
    path('', views.post_view, name='post_view'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
] 


