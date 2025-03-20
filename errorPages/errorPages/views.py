from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import render
from .forms import productoForm

class ProductoViewset(viewsets.ModelViewSet):
    #esta variable me dice de donde saco el modelo y la información
    queryset = Producto.objects.all()
    
    #Como serializar la información
    serializer_class = ProductoSerializer
    
    #Como renderizar mis respuestas
    renderer_classes = [JSONRenderer]
    
    #Permitir filtrar que métodos HTTP se pueden usar
    #GET, POST, PUT, DELETE
    #Por defecto si no lo declaro, se usan todos
    #http_method_names = ['GET', 'POST']

def agregar_view(request):
    form = productoForm()
    return render (request, 'agregar.html', {'form':form})
