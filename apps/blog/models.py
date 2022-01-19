from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        'Nombre', max_length=100, unique=True, null=False, blank=False)
    estado = models.BooleanField('Activa/No Activa', default=True)
    fecha_creacion = models.DateTimeField(
        'Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(
        'Nombre de usuario', max_length=100, unique=True, null=False, blank=False)
    nombres = models.CharField(
        'Nombres', max_length=100, null=False, blank=False)
    apellidos = models.CharField(
        'Apellidos', max_length=100, null=False, blank=False)
    email = models.EmailField(
        'Email', max_length=100, unique=True, null=False, blank=False)
    estado = models.BooleanField('Activo/No Activo', default=True)
    fecha_creacion = models.DateTimeField(
        'Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'
        ordering = ['nombre_usuario']

    def __str__(self):
        return self.nombre_usuario


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        'Titulo', max_length=100, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField(
        'Descripcion', max_length=150, blank=False, null=False)
    imagen_portada = models.URLField(
        'Imagen de Portada', max_length=255, blank=False, null=False)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField(
        'Fecha de Creacion', blank=False, null=False, auto_now_add=True, auto_now=False)
    contenido = RichTextField('Contenido')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'posts'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
