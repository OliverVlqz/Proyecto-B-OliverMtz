from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer
from .forms import alumnoForm
from django.shortcuts import render

class AlumnoViewset(viewsets.ModelViewSet):
    #esta variable me dice de donde saco el modelo y la información
    queryset = Alumno.objects.all()
    
    #Como serializar la información
    serializer_class = AlumnoSerializer
    
    #Como renderizar mis respuestas
    renderer_classes = [JSONRenderer]
    
    #Permitir filtrar que métodos HTTP se pueden usar
    #GET, POST, PUT, DELETE
    #Por defecto si no lo declaro, se usan todos
    #http_method_names = ['GET', 'POST']


def agregar_alumno (request):
    form = alumnoForm()
    return render (request, 'santibanez_lizbeth.html', {'form': form})