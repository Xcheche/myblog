from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    # posts = Post.Published.all()  wrong
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    # paginator class
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    return render(
        request, "blog/post/list.html", {"posts": posts}
    )  # Correctly rendering the post list template


def post_detail(request, id, year, month, day):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(
        request, "blog/post/detail.html", {"post": post}
    )  # Correctly rendering the post detail template
