from django.urls import path
from .views import *

urlpatterns=[
    path('api/get', lista_categorias, name='lista'),
    path('ver/', ver_categoria, name='ver'),
    path('registrar/', agregar_categoria, name='agregar')
]