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
        fields = ['nom_paq', 'nom_recep', 'cel_recep', 'peso', 'direccion', 'fec_reti', 'cantidad', 'detalles_paq']
        widgets = {
            'fec_reti': forms.DateInput(attrs={'type': 'date'}),
        }