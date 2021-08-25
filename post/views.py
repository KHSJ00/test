from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Post, Comment
from .forms import PostForm
from django.http import HttpResponse

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'post/post_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post/post_list.html', {'posts': posts})

def post_list_staff(request):
    all_posts = Post.objects.all().order_by('-published_date')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_posts, 7)
    posts = paginator.get_page(page)
    return render(request, 'post/post_list_staff.html', {'posts': posts})

def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk)
    if request.method == "POST":
        comment = Comment()
        comment.post = post_detail
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.author = request.user
        comment.save()
    return render(request, 'post/post_detail.html', {'post': post_detail, 'comments': comments})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'post/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'post/post_edit.html', {'form': form})

def post_not_allowed(request):
    return render(request, 'post/post_not_allowed.html')


def post_detail_staff(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk)
    if request.method == "POST":
        comment = Comment()
        comment.post = post_detail
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.author = request.user
        comment.save()
    return render(request, 'post/post_detail_staff.html', {'post': post_detail, 'comments': comments})

def post_list(request):
    if not request.user.is_authenticated:
        return render(request, 'post/post_must_login.html')
    else:
        all_posts = Post.objects.all().order_by('-published_date')
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        page = int(request.GET.get('p', 1))
        paginator = Paginator(all_posts, 7)
        posts = paginator.get_page(page)
        return render(request, 'post/post_list.html', {'posts': posts})