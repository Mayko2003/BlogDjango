from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginUsuario.as_view(), name='login'),
    path('logout', LogoutUsuario.as_view(), name='logout'),
    path('registrar', RegistroUsuario.as_view(), name='registrar')
]
