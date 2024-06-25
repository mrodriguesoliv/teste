from blog.models import Post
from django.shortcuts import render, redirect
from .forms import FormularioPost
from blog.models import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .admin import CustomUserCreationForm
from django.contrib import messages

PER_PAGE = 9


def post_view(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_view.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
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


def register(request):
        form = CustomUserCreationForm()
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
    
            if form.is_valid():
                user = form.save(commit=False)
                user.is_valid = False
                user.save()
                messages.success(request, 'Registrado. Agora faça o login para começar!')
                return redirect('blog:post_new')

            else:
                print('invalid registration details')
                
        return render(request, "registration/register.html",{"form": form})


