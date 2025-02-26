from django.shortcuts import render
from .models import Producto
from django.http import JsonResponse
from .forms import ProductoForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
import json


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

#Funcion que agrega un producto con un objeto JSON
def registrar_producto(request):
    #Ver si la peticion es de tipo POST
    if request.method == 'POST':
        try:
            data= json.loads(request.body)
            producto = Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            ) #Create mete directamente el objeto en la BD
            return JsonResponse({'mensaje':'Producto registrado correctamente', 'id': producto.id }, status=201)
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'error': str(e)}, status=400
            )
    return JsonResponse({'error':'No se permiten peticiones de ese tipo'}, status=405)
        
    
  #Funcion para el metodo PUT
def actualizar_producto(request, id_producto):
        if request.method == 'PUT':
            producto = get_object_or_404(Producto, id=id_producto)
            try:
                # La informacion de modificacion del producto viene en el body de la request
                data = json.loads(request.body)
                producto.nombre = data.get('nombre', producto.nombre)
                producto.precio = data.get('precio', producto.precio)
                producto.imagen = data.get('imagen', producto.imagen)
                producto.save()
                return JsonResponse({'mensaje':'Producto actualizado correctamente'}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'error':'No se permiten peticiones de ese tipo'}, status=405)
                
                
    
    #Funcion para el metodo DELETE
def borrar_producto(request, id_producto):
        if request.method == 'DELETE':
            producto = get_object_or_404(Producto, id=id_producto)
            producto.delete()
            return JsonResponse({'mensaje':'Producto eliminado correctamente'}, status=200)
        return JsonResponse({'error':'No se permiten peticiones de ese tipo'}, status=405)
      
    #Funcion adicional para GET
def obtener_producto(request, id_producto):
        if request.method == 'GET':
            producto = get_object_or_404(Producto, id=id_producto)
            data = {
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'imagen': producto.imagen
            }
            return JsonResponse(data, status=200)
        return JsonResponse({'error':'No se permiten peticiones de ese tipo'}, status=405)
    
    
    #De retornar un producto especifico 