from django.shortcuts import render, get_object_or_404
# 有用到時間函數
from .models import Post
# The dot before models means current directory or current application.
from django.utils import timezone



def post_list(request):
     # In the render function we have one parameter request
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})