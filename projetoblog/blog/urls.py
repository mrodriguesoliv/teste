from blog.views import (Teste)
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', Teste.as_view(), name='teste'),
    
    ]