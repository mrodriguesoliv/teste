from blog.models import Post, Usuario
from django.shortcuts import render, redirect
from .forms import FormularioPost, SignUpForm, LoginForm
from blog.models import timezone
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, get_user_model


def post_view(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_view.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
         form = FormularioPost()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = FormularioPost(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = FormularioPost(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def signup(request):
    usuario = Usuario.objects.get(id=1)
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            usuario.save()
            return redirect('blog:post_view')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('blog:post_view') 
            else:
                messages.error(request, 'Nome de usuário ou senha incorretos.')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})