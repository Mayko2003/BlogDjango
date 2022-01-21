from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import *
# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(estado=True)
    paginate_by = 3
    page_kwarg = 'page'
    def get_queryset(self):
        # se obtiene el queryset por defecto
        query = super().get_queryset()
        # se obtiene el parametro de busqueda
        buscar_p = self.request.GET.get('buscar_post')
        # se realiza el filtro de busqueda si es que existe el parametro
        if buscar_p:
            query = query.filter(
                Q(titulo__icontains=buscar_p) |
                Q(descripcion__icontains=buscar_p) |
                Q(creador__nombre_usuario=buscar_p)
            ).distinct()
        return query

class About(TemplateView):
    template_name = 'about.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class VerPost(DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'

class Explorar(ListView):
    model = Post
    template_name = 'explorar.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(estado=True)
    paginate_by = 3
    page_kwarg = 'page' 
    
    def get_queryset(self):
        # se obtiene el queryset por defecto
        query = super().get_queryset()
        # se realiza el filtro por una palabra
        buscar_p = self.request.GET.get('buscar_filtro')
        if buscar_p:
            query = query.filter(
                Q(titulo__icontains=buscar_p) |
                Q(descripcion__icontains=buscar_p) |
                Q(creador__nombre_usuario__exact=buscar_p)
            ).distinct()
        # se realiza el filtro por las categorias seleccionadas
        categorias_filter = self.request.GET.getlist('filter_cats')
        if categorias_filter:
            for cat in categorias_filter:
                query = query.filter(categorias__nombre__exact=cat).distinct()
        # se realiza el filtro por algun campo y algun orden
        orden_por_p = self.request.GET.get('orden_por')
        orden_p = self.request.GET.get('orden')
        if orden_p != None and orden_por_p:
            query = query.order_by(orden_p + orden_por_p)
        return query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['selec_cats'] = self.request.GET.getlist('filter_cats')
        return context
