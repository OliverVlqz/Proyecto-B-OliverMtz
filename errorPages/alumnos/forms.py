from django import forms
from .models import Alumno

class alumnoForm(forms.ModelForm): 

    class Meta:
        model = Alumno

        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']

        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Nombre del alumno'
                }
            ),
            'apellido' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'apellidos',
                }
            ),
            'edad' : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Edad del alumno'
                }
            ),
            'matricula' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Matricula Alumno',
                }
            ),
            'correo' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Correo',
                }
            ),
            
        }

        #Etiquetas personalizadas 
        labels = {
            'nombre' : 'Nombre del Alumno',
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre' : {'required' : 'El nombre es obligatorio'},
            'matricula' : {'required' : 'La matrícula debe ser única', 'invalid' : 'Ingrese un correo diferente'}
        }