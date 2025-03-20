#Generar aqui todos los formularios HTML que vamos a ocupar

from django import forms 
from .models import Producto

#Crear una clase para cada formulario que necesitemos
class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        
        #Campos que se verán en el formulario
        fields= ['nombre', 'precio', 'imagen']
        
        #Personalizar mis inputs
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese aquí su nombre de producto',
                }
            ),
            'precio': forms.TextInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Ingrese el precio'
                }
            ),
            'imagen': forms.TextInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Ingrese su url'
                }
            )
        }
        
        #Etiquetas
        labels ={
            'nombre' : 'Nombre del producto',
            'precio' : 'Precio (MXN)',
            'imagen' : 'URL de la imagen'
        }
        
        #Personalizar los mensajes de error
        error_messages ={
            'precio' : {'required': 'El precio no puede estar vacío',
            'invalid': 'Ingresa un precio válido'            
            }
        }