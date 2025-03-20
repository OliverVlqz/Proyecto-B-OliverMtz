import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm



class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': True,
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número'
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': True
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                    'required': True,
                    'pattern': '^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$',
                    'title': 'Correo de la UTEZ'
                }
            ),
            'name': forms.TextInput(
                attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'required': True
            }
            ),
            'surname': forms.TextInput(
                attrs={
            'class': 'form-control',
            'placeholder': 'Surname',
            'required': True
            }),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Control number',
                    'required': True,
                    'pattern': '^\d{5}[a-zA-Z]{2}\d{3}$',
                    'title': 'La matrícula debe ser de la UTEZ',
                    'maxlength': 20
                }
            ),
            'age': forms.NumberInput(
                attrs={
                'class': 'form-control',
                'required': True,
                'pattern': '^[0-9]+$',
                'max': '100',
                'min': '1'
            }),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone number',
                    'required': True,
                    'pattern': '^[0-9\+-]{10,}$',
                    'title': 'El número telefónico debe ser de 10 dígitos.',
                    'maxlength': '15'
                }
            ),
        }
    
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        if len(name) > 100:
            raise forms.ValidationError("El nombre no puede exceder los 100 caracteres.")
        return name
    
    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if len(surname) < 3:  
            raise forms.ValidationError("El apellido debe tener al menos 3 caracteres.")
        if len(surname) > 100:
            raise forms.ValidationError("El apellido no puede exceder los 100 caracteres.")
        return surname



    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@utez.edu.mx"):
            raise forms.ValidationError("El correo debe ser institucional de UTEZ")
        return email
        

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        
        pattern = r'^[0-9]{5}[a-zA-Z]{2}[0-9]{3}$' 
        if not re.match(pattern, control_number):
            raise forms.ValidationError("La matrícula debe tener el formato correcto de UTEZ")
        
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        pattern = r'^[0-9]{10}$'  
        if not re.match(pattern, tel):
            raise forms.ValidationError("El número de teléfono debe contener 10 dígitos")
        return tel
    
    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18 or age > 40: 
            raise forms.ValidationError("La edad debe estar entre 18 y 40 años")
        return age

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
        
        if not re.match(pattern, password1):
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres, 1 número, 1 letra mayúscula y 1 carácter especial " 
            )
        
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data



#Segundo formulario (inicio de sesión)
class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Correo electrónico", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
def clean(self):
    cleaned_data = super().clean()
    username = cleaned_data.get("username")
    password = cleaned_data.get("password")
    if username and password:
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Usuario o contraseña incorrectos.")
    return cleaned_data