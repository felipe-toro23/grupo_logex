from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CreaUsuForm, PaqueteForm
from .models import Usuarios, Direcciones, Paquetes, PlanillasEntregas, PlanillaRetiros
from django.contrib import messages
from django.db import IntegrityError, DataError




def index(request):
    return render(request, "logex/home.html")


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
                form.add_error('username', 'Este nombre de usuario ya está en uso. Por favor, elige otro.')#revisar este error

            except DataError as e:
                messages.error(request, 'Error al crear la cuenta: los datos son demasiado largos.') #revisar este error

    else:
        form = CreaUsuForm()

    return render(request, "logex/crear_cuenta.html", {'form': form})


@login_required
def profile(request):
    #crea in if que envie a otra pagina si es super usuario
    if request.user.is_superuser:
        return render(request, "superusuario/entregas.html")
    else:
        return render(request, "logex/loby.html")


def salir(request):
    logout(request)
    return redirect('/')


@login_required
def guardar_paquete(request):
    if request.method == "POST":
        form = PaqueteForm(request.POST)

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

                if request.user.is_authenticated:
                    username_autentic = request.user.username

                usuario = get_object_or_404(Usuarios, username=username_autentic)


                

                nom_paq = form.cleaned_data['nom_paq']
                nom_recep = form.cleaned_data['nom_recep']
                cel_recep = form.cleaned_data['cel_recep']
                fec_reti = datetime.now() + timedelta(days=1)
                detalles_paq = form.cleaned_data['detalles_paq']

                # guarda los datos en la tabla Paquetes y Direcciones, recuerda que esta basado en el models usuario
                nuevo_paquete = Paquetes.objects.create(
                    cuenta=usuario,
                    nom_paq=nom_paq,
                    nom_recep=nom_recep,
                    cel_recep=cel_recep,
                    direccion=direccion,
                    fec_reti=fec_reti,
                    detalles_paq=detalles_paq
                )


                return render(request, "logex/Listado_encomiendas.html")
            except IntegrityError as e:
                form.add_error('username', 'Este nombre de usuario ya está en uso. Por favor, elige otro.')
    else:
        form = PaqueteForm()

    return render(request, "logex/nueva_encomienda.html", {'form': form})
                                            

def encomiendas(request):

    usuario = get_object_or_404(Usuarios, username=request.user.username)
    paquetes = Paquetes.objects.filter(cuenta=usuario).select_related('direccion')


    data = {
        'Paquetes': paquetes
    }

    return render(request, "logex/Listado_encomiendas.html", data)

def eliminar_cliente(request, id_cliente):
    cliente = Usuarios.objects.get(id_cuenta=id_cliente)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('verclientes')  # Redirigir a la lista de clientes después de la eliminación
    
    return render(request, 'superusuario/clientes.html', {'cliente': cliente})

def entregasupuser(request):
    fecha_inicio = request.GET.get('fecha_inicio', None)
    fecha_fin = request.GET.get('fecha_fin', None)

    paquetes = Paquetes.objects.all()

    if fecha_inicio and fecha_fin:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
        paquetes = paquetes.filter(fec_reti__range=(fecha_inicio, fecha_fin))

    data = {
        'Paquetes': paquetes
    }

    return render(request, "superusuario/entregas.html", data)

def verclientes(request):
    clientes = Usuarios.objects.filter(is_superuser=False)

    data = {
        'clientes': clientes
    }

    return render(request, "superusuario/clientes.html", data)
