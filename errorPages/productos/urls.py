from django.urls import path
from .views import *

urlpatterns=[
    path('api/get', lista_productos, name='lista'),
    path('ver/', ver_producto, name='ver'),
    path('agregar/', agregar_producto, name='agregar')
]