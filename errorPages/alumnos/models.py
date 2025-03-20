from django.db import models

# Clase de Producto
class Alumno(models.Model):
    #atributos de clase
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=50, unique=True)
    correo = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.nombre
    
    #Necesito una función que devuelva el objeto en forma de diccionario (Dict)
    def to_ditc(self):
        return{
            # 'claveValor' : 'valor'
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'matricula': self.matricula,
            'correo': self.correo
        }
