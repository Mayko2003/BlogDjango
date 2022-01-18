from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

# Register your custom resources here

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario
        
class PostResource(resources.ModelResource):
    class Meta:
        model = Post

# Register your custom admin models here.

class CategoriaAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'estado', 'fecha_creacion']
    resource_class = CategoriaResource

class UsuarioAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_usuario', 'nombres', 'apellidos', 'email']
    list_display = ['nombre_usuario', 'nombres', 'apellidos', 'email', 'estado', 'fecha_creacion']
    resource_class = UsuarioResource

class PostAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ['titulo', 'creador', 'descripcion', 'estado', 'fecha_creacion']
    resource_class = PostResource

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Post, PostAdmin)

