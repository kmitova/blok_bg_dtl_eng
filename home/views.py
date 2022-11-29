from django.shortcuts import render, redirect

from home.forms import PostCreateForm
from home.models import Post


def home_page(request):
    posts = Post.objects.all()
    print(posts)
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard.html', context)


def notifications_page(request):
    return render(request, 'notifications.html')


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