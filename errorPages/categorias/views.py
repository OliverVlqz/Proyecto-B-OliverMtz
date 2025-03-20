from django.shortcuts import render, redirect
from .models import Categoria
#Este Objeto me permite enviar respuesta JSON
from django.http import JsonResponse

from .forms import categoriaForm

# Create your views here.

#Una vista que cargue y maneje al mismo tiempo el formulario
def agregar_categoria(request):
    #checar si vengo del formulario
    if request.method == 'POST':
        #Quiere decir que enviaron el form
        form = categoriaForm(request.POST)
        #Checar que sus datos estén bien
        if form.is_valid():
            #lo guardo en bd
            form.save()
            return redirect('verCategoria')
        #Que pasa si no fue que mandaron el form
    else:
            form = categoriaForm
    return render(request, 'agregarCategoria.html',{'form': form})

#Vista que devuelve los productos como json
def lista_categorias(request):
    #Obtener todos los objetos de productos de la bd
    categorias = Categoria.objects.all()
    
    #Vamos a guardar los datos en un diccionario
    #Este diccionario fue creado al aire y no es seguro
    data = [
        {
            'nombre': p.nombre,
            'imagen': p.imagen
        }
        for p in categorias
    ]
    return JsonResponse(data, safe=False)

def ver_categorias(request):
    return render(request, 'verCategoria.html')


import json
#Función que agrega un producto con un objeto JSON
def registrar_categoria(request):
    #Checa si muestra request es de tipo POST
    if request.method == 'POST':
        #quiere decir que si estoy manejando el request
        try:
            data = json.loads(request.body) #Parametro es un texto que debería ser un JSON
            categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            ) #Create directamente mete el objeto en la BD
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso',
                    'id': categoria.id    
                }, status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'error': str(e)}, status = 400
            )
    #Si no es POST el request...
    return JsonResponse (
        {'error': 'El método no es soportado'}, status = 405
    )