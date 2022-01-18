from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    posts = Post.objects.filter(estado = True)
    query = request.GET.get("buscar_post")
    if query:
        posts = Post.objects.filter(
            Q(titulo__icontains = query) |
            Q(descripcion__icontains = query)
        ).distinct()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts' : posts})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def ver_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'post' : post})