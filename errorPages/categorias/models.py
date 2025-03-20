from django.db import models

# Clase de Categoria
class Categoria(models.Model):
    #atributos de clase
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()
    
    def __str__(self):
        return self.nombre
    
    #Necesito una función que devuelva el objeto en forma de diccionario (Dict)
    def to_ditc(self):
        return{
            # 'claveValor' : 'valor'
            'nombre': self.nombre,
            'imagen': self.imagen
        }
