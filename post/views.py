from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def post_index(request):
    post_list = Post.objects.all()
    # filter
    query = request.GET.get("search")
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(user__first_name__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    context = {"posts": posts}
    return render(request, "post/index.html", context)


def post_create(request):
    if not request.user.is_authenticated:
        return Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, "Başarılı bir şekilde oluşturuldu!")
        return render(request, "post/detail.html", {"post": post})
    context = {
        "form": form,
    }
    return render(request, "post/form.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return render(request, "post/detail.html", {"post": post})
    context = {
        "post": post,
        "form": form,
    }
    return render(request, "post/detail.html", context)


def post_update(request, id):
    if not request.user.is_authenticated:
        return Http404
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde değiştirildi!")
        return render(request, "post/detail.html", {"post": post})
    context = {
        "form": form,
    }
    return render(request, "post/form.html", context)


def post_delete(request, id):
    if not request.user.is_authenticated:
        return Http404
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("post:index")
