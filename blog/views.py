from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Comment, Post


def index(request):
    posts = Post.objects.order_by('-creation_date')

    context = {
        'posts': posts
    }

    return render(request, 'blog/index.html', context)


def post_create(request):
    title = request.POST.get('title').strip()
    content = request.POST.get('content').strip()

    if not title or not content:
        return render(request, 'blog/new.html', {
            'error_message': 'Introduce los datos del post para continuar',
        })

    post = Post(author=request.user, title=title, content=content)
    post.save()

    return HttpResponseRedirect(reverse('index'))


@login_required
def post_new(request):
    context = {}
    return render(request, 'blog/new.html', context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    context = {
        'post': post
    }

    return render(request, 'blog/detail.html', context)


def comment_create(request, post_id):
    content = request.POST.get('content').strip()

    if content:
        comment = Comment(author=request.user, post=Post.objects.get(
            pk=post_id), content=content)
        comment.save()

    return HttpResponseRedirect(reverse('post_detail', args=[post_id]))
