from django import forms
from .models import Post, Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model



class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")


class LoginForm(AuthenticationForm):
    pass


class FormularioPost(forms.ModelForm):
    class Meta:
      model = Post
      fields = ('title', 'body', 'cover')