from django.shortcuts import render
from .models import Categoria
from django.http import JsonResponse
from .forms import CategoriaForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
import json


# Create your views here.
def lista_categorias(request):
    categorias = Categoria.objects.all()
    data =[
        {
            "nombre": c.nombre,
            "imagen": c.imagen
        }
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def ver_categoria(request):
    return render(request, 'verCategoria.html')

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = CategoriaForm()
    return render(request, 'agregar.html', {'form': form})
    
def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            categoria = Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            )
            return JsonResponse({'mensaje':'Categoria registrada correctamente', 'id': categoria.id}, status=201)
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'error': str(e)}, status=400
            )
    return JsonResponse({'error':'No se permiten peticiones de ese tipo'}, status=405)

