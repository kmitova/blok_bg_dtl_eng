from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from home.forms import PostCreateForm, CommentForm, ReplyForm
from home.models import Post, Comment, SupportPost

UserModel = get_user_model()


def home_page(request):
    posts = Post.objects.all()


    context = {
        'posts': posts,
        'post-form': PostCreateForm(),
        'comment_form': CommentForm(),
        'reply_form': ReplyForm(),
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
def reply_to_comment(request,  post_id, comment_id):
    comment = Comment.objects.filter(pk=comment_id).get()
    post = Post.objects.filter(pk=post_id).get()

    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)

        reply.comment = comment
        reply.post = post
        # print(post)
        reply.user = request.user
        reply.save()

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


def support_post(request, post_id):
    post = Post.objects.filter(pk=post_id).get()
    support_object = SupportPost.objects.filter(related_post_id=post_id).first()

    if support_object:
        support_object.delete()
    else:
        support = SupportPost(related_post=post)
        support.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{post_id}')


