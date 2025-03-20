#Generar aqui todos los formularios HTML que vamos a ocupar

from django import forms 
from .models import Categoria

#Crear una clase para cada formulario que necesitemos
class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        
        #Campos que se verán en el formulario
        fields= ['nombre', 'imagen']
        
        #Personalizar mis inputs
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese aquí el nombre de su categoría',
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
            'nombre' : 'Nombre de la categoría',
            'imagen' : 'URL de la imagen'
        }
        
        #Personalizar los mensajes de error
        error_messages ={
            'nombre' : {'required': 'El nombre no puede estar vacío',
            'invalid': 'Ingresa un nombre válido'           
            }
        }