
from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']
        labels = {
            'nombre': 'Nombre de la categoría',
            'imagen': 'URL de la imagen'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre de la categoría'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'URL de la imagen'
                }
            )
        }
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio'
            },
            'imagen': {
                'required': 'Este campo es obligatorio'
            }
        }