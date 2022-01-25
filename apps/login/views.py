from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistroUsuarioForm
from django.views.generic import CreateView
from apps.blog.models import Usuario
# Create your views here.

class LoginUsuario(LoginView):
    template_name = 'usuario/login.html'
    next_page = reverse_lazy('blog_urls:home')
    redirect_authenticated_user = True
    
class LogoutUsuario(LogoutView):
    next_page = reverse_lazy('blog_urls:home')

class RegistroUsuario(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'usuario/registrar.html'
    success_url = reverse_lazy('login_urls:login')