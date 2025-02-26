from django.urls import path
from .views import *

urlpatterns=[
    path('api/get', lista_productos, name='lista'),
    path('ver/', ver_producto, name='ver'),
    path('agregar/', agregar_producto, name='agregar'),
    path('api/post/', registrar_producto, name='post'),
    path('api/put/<str:id_producto>/', actualizar_producto, name='put'),
    path('api/delete/<str:id_producto>/', borrar_producto, name='delete'),
    path('api/get/<str:id_producto>/', obtener_producto, name='get')
]