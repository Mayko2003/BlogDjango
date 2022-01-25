from django.contrib.auth.forms import UserCreationForm
from apps.blog.models import Usuario
from django import forms
class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    class Meta:
        model = Usuario
        fields = ['username','first_name', 'last_name', 'email']
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombres',
            'last_name' : 'Apellidos',
            'email' : 'Correo electronico',
        }
        