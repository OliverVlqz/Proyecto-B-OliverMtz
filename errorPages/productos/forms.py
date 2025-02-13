#Aqui se generan todos los formularios HTML que se utilizarán en la aplicación.

from django import forms
from .models import Producto


#Crear una clase para cada formulario que necesitemos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'imagen': 'URL de la imagen'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Precio del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'URL de la imagen'
                }
            )
        }
        #Etiquetas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen'
        }
        #Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio'
            },
            'precio': {
                'required': 'Este campo es obligatorio',
                'invalid': 'Por favor, escribe un número válido'
            },
            'imagen': {
                'required': 'Este campo es obligatorio'
            }
        }