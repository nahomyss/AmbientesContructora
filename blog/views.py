from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def contact(request):
    return render(request, 'blog/contact.html', {})


def about(request):
    return render(request, 'blog/about.html', {})


def detailPalacio(request):
    return render(request, 'blog/detailProject/palacioDetail.html', {})
