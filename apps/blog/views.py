from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    posts = Post.objects.filter(estado=True)
    query = request.GET.get("buscar_post")
    if query:
        posts = Post.objects.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(creador__nombre_usuario=query)
        ).distinct()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def ver_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post': post})



def explorar(request):

    # inicializacion de las variables
    categorias = Categoria.objects.all()  # todas las categorias
    posts = Post.objects.filter(estado=True)  # todos los posts publicados
    
    # se obtiene el parametro de busqueda y se la realiza
    query = request.GET.get("buscar_filtro")
    if query:
        posts = Post.objects.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query)
        ).distinct()

    # filtrar por categoria
    categorias_filter = request.GET.getlist('filter_cats')
    if categorias_filter:
        for cat in categorias_filter:
            posts = posts.filter(categorias__nombre__exact=cat).distinct()

    # se obtiene los parametros de ordenamiento
    orden_por = request.GET.get("orden_por")
    orden = request.GET.get("orden")
    # se ordena por los parametros
    if orden_por and orden != None:
        posts = posts.order_by(orden + orden_por)

    # paginacion
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # renderizacion
    return render(request, 'explorar.html', {'categorias': categorias, 'posts': posts, 'selec_cats': categorias_filter})
