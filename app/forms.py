from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Paquetes, PlanillasEntregas, Direcciones
from datetime import datetime, timedelta


COMUNAS_CHOICES = [
    ('LC', 'Las Condes'),
    ('PR', 'Providencia'),
    ('ST', 'Santiago'),
    ('VC', 'Vitacura'),
    ('LR', 'La Reina'),
    ('NU', 'Ñuñoa'),
    ('MP', 'Maipú'),
    ('QC', 'Quilicura'),
    ('PA', 'Puente Alto'),
    ('LP', 'La Pintana'),
    ('RE', 'Renca'),
    ('HU', 'Huechuraba'),
    ('SM', 'San Miguel'),
    ('IN', 'Independencia')
]

class CreaUsuForm(forms.Form):
    rut = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut'})
    )

    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario'})
    )

    nombre = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    apellido = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )
    direccion_calle = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle'})
    )
    direccion_numeracion = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numeración'})
    )
    direccion_comuna = forms.ChoiceField(
        choices=COMUNAS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )


class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquetes
        fields = ['nom_paq', 'nom_recep', 'cel_recep', 'direccion_calle', 'direccion_numeracion', 'direccion_comuna', 'detalles_paq']

    nom_paq = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del paquete'})
    )
    
    nom_recep = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del receptor'})
    )
    
    cel_recep = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Celular del receptor'})
    )
    
    direccion_calle = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle'})
    )
    direccion_numeracion = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numeración'})
    )
    direccion_comuna = forms.ChoiceField(
        choices=COMUNAS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    detalles_paq = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Detalles del paquete'})
    )