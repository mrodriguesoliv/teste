from django.contrib import admin
from .models import Post, Usuario
from django.contrib.auth.admin import UserAdmin


admin.site.register(Post)
admin.site.register(Usuario, UserAdmin)