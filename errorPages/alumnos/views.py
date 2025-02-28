from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer
from .forms import AlumnoForm
from django.shortcuts import render, redirect
# Create your views here.

class AlumnoViewSet(viewsets.ModelViewSet):
    #Me dice de donde saco el modelo y la informacion de la BD
    queryset = Alumno.objects.all()
    #Como serializar la informacion
    serializer_class = AlumnoSerializer
    #Como se va a renderizar la informacion
    renderer_classes = [JSONRenderer]
    #GET POST, PUT, DELETE
    
#Crea una funcion que reciba los datos del formulario y los retorne a la pagina de Martinez_Oliver.html
def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_alumno')
    else:
        form = AlumnoForm()
    return render(request, 'Martinez_Oliver.html', {'form': form})
