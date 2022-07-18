from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def page_not_found_view(request, exception):
    return render(request, 'posts/404.html', {"path": request.path}, status=404)


def server_error(request):
    return render(request, 'posts/500.html', status=500)


@login_required
def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Post has been planted!')
            return redirect('posts:index')
    else:
        form = PostForm(initial={'author': request.user.pk})
    context = {'form': form}
    return render(request, 'posts/post_add.html', context)
