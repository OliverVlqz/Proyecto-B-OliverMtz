from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    #Me dice de donde saco el modelo y la informacion de la BD
    queryset = Producto.objects.all()
    #Como serializar la informacion
    serializer_class = ProductoSerializer
    #Como se va a renderizar la informacion
    renderer_classes = [JSONRenderer]
    #GET POST, PUT, DELETE
    # http_method_names = ['get', 'post', 'put', 'delete']
    
    
    