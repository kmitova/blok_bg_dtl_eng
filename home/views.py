from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from home.forms import PostCreateForm, CommentForm
from home.models import Post

UserModel = get_user_model()
def home_page(request):
    posts = Post.objects.all()
    print(posts)
    post7 = posts.filter(pk=7).get()
    print(post7)
    # print(post7.comment_set.all())
    context = {
        'posts': posts,
        'post-form': PostCreateForm(),
        'comment_form': CommentForm(),
    }
    return render(request, 'dashboard.html', context)


def notifications_page(request):
    return render(request, 'notifications.html')


@login_required
def comment_post(request, post_id):
    post = Post.objects.filter(pk=post_id).get()

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

    return redirect('home page')


@login_required
def make_post(request):
    if request.method == "GET":
        form = PostCreateForm()
    else:
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'dashboard.html', context)