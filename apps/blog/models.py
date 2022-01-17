from django.db import models

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now=False ,auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categorias'
        
    def __str__(self):
        return self.nombre
    

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField('Nombre de usuario',max_length=100, unique=True, null=False, blank=False)
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now=False ,auto_now_add=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'
        
    def __str__(self):
        return "{nombres} {apellidos}".format(nombres=self.nombres, apellidos=self.apellidos)
    

    

    
