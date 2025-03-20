from django.urls import path
from . views import *

urlpatterns= [
    path('api/get', lista_categorias, name='lista'),
    path('json/', ver_categorias, name='verCategoria'),
    path('registrar/', agregar_categoria, name= 'agregar'),
    path('api/post/', registrar_categoria, name= 'post'),
]