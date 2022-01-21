from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('about', About.as_view(), name = 'about'),
    path('contact', Contact.as_view(), name = 'contact'),
    path('ver-post/<slug:slug>', VerPost.as_view(), name = 'ver_post'),
    path('explorar', Explorar.as_view(), name = 'explorar'),
]
