from blog.models import Post
from django.shortcuts import render, redirect
from .forms import FormularioPost
from blog.models import timezone
from django.urls import reverse

PER_PAGE = 9

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