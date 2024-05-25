from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_view, name='post_view'),
    path('post/<int:pk>/', views.testess, name='testess'),
]
