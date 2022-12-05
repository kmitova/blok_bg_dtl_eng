from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from core.utils import get_group_users, get_group_posts
from dmmessages.models import Chat
from home.forms import PostCreateForm, CommentForm, ReplyForm, AnnouncementForm
from home.models import Post, Comment, SupportPost

UserModel = get_user_model()


@login_required
def home_page(request):
    current_user = request.user
    users = get_group_users(request)
    posts = get_group_posts(request)

    query = request.GET.get('query')
    query_made = False
    if query != '' and query is not None:
        posts = posts.filter(Q(user__first_name__icontains=query) |
                             Q(user__last_name__icontains=query) |
                             Q(content__icontains=query)).distinct()
        query_made = True

    # chats = Chat.objects.all()

    context = {
        'current_user': current_user,
        'posts': posts,
        'users': users,
        'post-form': PostCreateForm(),
        'comment_form': CommentForm(),
        'reply_form': ReplyForm(),
        'query_made': query_made,
        'is_dashboard': True,
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


@login_required
def make_announcement(request):
    if request.method == "GET":
        form = AnnouncementForm()
    else:
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'admin/announcement-page.html', context)


@login_required
def support_post(request, post_id):
    post = Post.objects.filter(pk=post_id).get()
    support_object = SupportPost.objects.filter(related_post_id=post_id).first()

    if support_object:
        support_object.delete()
    else:
        support = SupportPost(related_post=post)
        support.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{post_id}')


