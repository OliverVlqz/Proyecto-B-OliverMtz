from django.db import models

# Create your models here.
# modelo Django de alumnos:

# Nombre
# Apellido
# Edad
# Matricula (único)
# Correo (único)

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido