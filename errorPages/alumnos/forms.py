from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['id','nombre','apellido', 'edad', 'correo', 'matricula']
        labels = {
            'id': 'ID del alumno',
            'nombre': 'Nombre del alumno',
            'apellido': 'Apellido del alumno',
            'edad': 'Edad del alumno',
            'correo': 'Correo del alumno',
            'matricula': 'Matricula del alumno'
        }
        widgets = {
            'id': forms.TextInput(
                attrs={ 
                    'class': 'form-input',
                    'placeholder': 'ID del alumno'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre del alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Apellido del alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Edad del alumno'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Correo del alumno'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Matricula del alumno'
                }
            )
        }