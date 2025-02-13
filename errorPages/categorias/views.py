from django.shortcuts import render
from .models import Categoria
from django.http import JsonResponse
from .forms import CategoriaForm
from django.shortcuts import redirect


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
    
    