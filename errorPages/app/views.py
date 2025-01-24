from django.shortcuts import render
from .utils import google_search
from django.http import JsonResponse
from django.shortcuts import render
from .models import ErrorLog

# Create your views here.

from django.http import HttpResponse 

#def index(request):
#   return HttpResponse("<h1>Hola Mundo!</h1>")
def index(request):
    return render(request, 'index.html', status=200)

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

def generar_error(request):
    return 1/0

def onePage(request):
    return render(request, 'onePage.html', status=200)

def prueba_front(request):
    #Obtener la informacion del html
    texto = request.GET.get('texto', 'No hay texto')
    
    #Vamos a generar informacion en python
    objeto1={
        "id":'001',
        "titulo": texto,
        "descripcion": "descripcion del primer titulo",
        
    }
    objeto2 ={
        'id':'002',
        'titulo': "segundo titulo",
        'descripcion': "descripcion del segundo titulo",
    }
    objeto3 ={
        'id':'003',
        'titulo': "tercer titulo",
        'descripcion': "descripcion del tercer titulo",
    }
    conjunto = [objeto1, objeto2, objeto3]
    #Como mandar un objeto (variable) de python a la vista:
    # #Obtener datos de la base de datos
    # personas = Usuarios.objects.values('id', 'nombres', 'apellidos', 'edad')
    # listaPersonas = list(personas)
    
   
    return render(request, 'prueba.html', {"objeto1":objeto1, 'arreglo':conjunto }, status=200)

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})