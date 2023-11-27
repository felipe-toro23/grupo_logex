from django.shortcuts import render, redirect
from .models import Usuarios, Direcciones, Paquetes
from .forms import CreaUsuForm, PaqueteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PlanillasEntregas, PlanillaRetiros
from datetime import datetime, timedelta



def index(request):
    return render(request, "logex/home.html")


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from .forms import CreaUsuForm

def Crear_cuenta(request):
    if request.method == "POST":
        form = CreaUsuForm(request.POST)
        if form.is_valid():
            try:
                direccion_calle = form.cleaned_data['direccion_calle']
                direccion_numeracion = form.cleaned_data['direccion_numeracion']
                direccion_comuna = form.cleaned_data['direccion_comuna']

                direccion, created = Direcciones.objects.get_or_create(
                    calle_dire=direccion_calle,
                    numeracio_dire=direccion_numeracion,
                    comuna_id=direccion_comuna
                )

                rut = form.cleaned_data['rut']
                nombre = form.cleaned_data['nombre']
                apellido = form.cleaned_data['apellido']
                correo = form.cleaned_data['correo']
                contrasena = form.cleaned_data['contrasena']
                username = form.cleaned_data['username']

                nuevo_usuario = Usuarios.objects.create_user(
                    username=username,
                    password=contrasena,
                    rut_cli=rut,
                    nombre_cli=nombre,
                    apellido_cli=apellido,
                    email=correo,
                    direcciones=direccion
                )

                return render(request, "logex/loby.html")
            except IntegrityError as e:
                form.add_error('username', 'Este nombre de usuario ya está en uso. Por favor, elige otro.')
    else:
        form = CreaUsuForm()

    return render(request, "logex/crear_cuenta.html", {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(f"Usuario autenticado: {user}")
                login(request, user)
                print("Inicio de sesión exitoso.")
                return HttpResponseRedirect(reverse('logex:profile'))
            else:
                print(f"Error de credenciales para usuario: {username}")
        else:
            print("Formulario no válido")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, "logex/loby.html")


def salir(request):
    logout(request)
    return redirect('/')

from django.shortcuts import render, redirect
from .forms import PaqueteForm



@login_required
def obtener_id_cuenta(request):
    usuario_actual = request.user

    direccion_usuario = usuario_actual.direcciones

    datos_remitente = {
        'id_cuenta': usuario_actual.id_cuenta,
        'rut_cli': usuario_actual.rut_cli,
        'nombre': usuario_actual.nombre_cli,
        'apellido': usuario_actual.apellido_cli,
        'direccion': {
            'calle': direccion_usuario.calle_dire,
            'numeracion': direccion_usuario.numeracio_dire,
            'comuna': direccion_usuario.comuna.comuna
        }
    }


    form = PaqueteForm(initial={
        'nom_recep': f"{usuario_actual.nombre_cli} {usuario_actual.apellido_cli}",
        'direccion': f"{direccion_usuario.calle_dire}, {direccion_usuario.numeracio_dire}, {direccion_usuario.comuna.comuna}",
    })

    return render(request, 'logex/nueva_encomienda.html', {'datos_remitente': datos_remitente, 'form': form})


@login_required
def guardar_paquete(request):
    if request.method == 'POST':
        form = PaqueteForm(request.POST)

        if form.is_valid():
            paquete = form.save(commit=False)

            paquete.remitente = request.user

            paquete.save()

            nueva_direccion = Direcciones.objects.create(
                calle=form.cleaned_data['direccion_calle'],
                numeracion=form.cleaned_data['direccion_numeracion'],
                comuna=form.cleaned_data['direccion_comuna'],
            )
            paquete.direccion = nueva_direccion
            paquete.save()

            return redirect('obtener_id_cuenta')  # Cambia 'nombre_de_tu_template' al nombre de tu template de éxito o a la URL que desees redirigir

    else:
        form = PaqueteForm()

    return render(request, 'logex/nueva_encomienda.html', {'form': form})



def encomiendas(request):
    pass