from django.db import models
from categorias.models import Categoria

class DetallesProducto(models.Model):
    descripcion = models.CharField(max_length=300)
    fecha_caducidad = models.DateField()
    
class Proveedor(models.Model):
    nombre =models.CharField(max_length=100)
    contacto = models.CharField(max_length=200)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

# Clase de Producto
class Producto(models.Model):
    #atributos de clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    #Primer parameto es el modelo a relacionar y despues la estrategia de borrado
    detalles_productos = models.OneToOneField(DetallesProducto, null=True, blank=True, on_delete=models.CASCADE)
    
    #Cuando se requiera usar una relacion
    #OneToOneField (1:1)
    #ForeignKey (1:M)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    #ManyToManyField (M:M)
    proveedor = models.ManyToManyField(Proveedor)
    
    def __str__(self):
        return self.nombre
    
    #Necesito una función que devuelva el objeto en forma de diccionario (Dict)
    def to_ditc(self):
        return{
            # 'claveValor' : 'valor'
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }

