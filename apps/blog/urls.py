from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = 'home'),
    path('about', about, name = 'about'),
    path('contact', contact, name = 'contact'),
    path('ver-post/<slug:slug>', ver_post, name = 'ver_post'),
    path('explorar', explorar, name = 'explorar'),
]
