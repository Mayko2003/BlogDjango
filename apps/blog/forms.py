from django import forms
from .models import *
from ckeditor.fields import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'imagen_portada', 'estado', 'categorias', 'contenido']
        labels = {
            'titulo' : 'Titulo',
            'descripcion' : 'Descripcion',
            'imagen_portada' : 'Imagen de Portada',
            'categorias' : 'Categorias'
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un titulo',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese una descripcion',
                }
            ),
            'imagen_portada': forms.URLInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el link de la imagen',
                    'required' : False
                }
            ),
            'estado' : forms.HiddenInput(),
            'categorias' : forms.SelectMultiple(
                attrs={
                    'class' : 'form-select'
                }
            ),
            'contenido' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                }
            )
        }
        