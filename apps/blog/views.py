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
    paginator = Paginator(posts, 3)
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


def explorar(request):
    # se obtienen todas las categorias y se crea una lista de indices
    categorias = Categoria.objects.all()
    indices = range(len(categorias))
    indices_categorias = zip(indices, categorias)
    
    # se obtienen los parametros de la peticion
    items = list(request.GET.items())
    # se obtienen todos los posts publicados
    posts = Post.objects.filter(estado = True)
    # se obtiene el parametro de busqueda y se realiza la busqueda
    query = request.GET.get("filtrar_post")
    if query:
        posts = Post.objects.filter(
            Q(titulo__icontains = query) |
            Q(descripcion__icontains = query)
        ).distinct()
    
    # si hay parametros se realiza el filtro
    if len(items) > 1:
        orden_por = request.GET.get("orden_por")
        orden = request.GET.get("orden")
        categorias = list()
        for i in range(3,len(items)):
            categorias += [items[i][1]]
        # filtrar por categoria
        if categorias:
            for cat in categorias:
                posts = posts.filter(categorias__nombre__exact = cat).distinct()
        # ordenar por los parametros
        posts = posts.order_by(orden + orden_por)
    
    # paginacion
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    # renderizacion
    return render(request, 'explorar.html', {'indices_categorias' : indices_categorias, 'posts' : posts})