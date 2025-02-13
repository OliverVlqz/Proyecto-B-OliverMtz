from django.db import models

# Clase de productos
class Producto(models.Model):
    # Atributos de la clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    
    def __str__(self):
        return self.nombre
    
    # Necesito una funcion que devuelva el objeto en forma de Dict
    def to_ditc(self):
        return{
            #'clave: valor'
            "nombre": self.nombre,
            "precio": self.precio,
            "imagen": self.imagen
        }
    