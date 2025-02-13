from django.shortcuts import render
from .models import Producto
from django.http import JsonResponse
from .forms import ProductoForm
from django.shortcuts import redirect


# Create your views here.
#Vista que devuelve los productos como json
def lista_productos(request):
    #Obtener todos los objetos de productos de la bd
    productos = Producto.objects.all()
    #Vamos a utilizar los datos en un diccionario
    data = [
        {
            "nombre": p.nombre,
            "precio": p.precio,
            "imagen": p.imagen
        }
        for p in productos
            
    ]
    
    return JsonResponse(data, safe=False)


def ver_producto(request):
    return render(request, 'ver.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})