from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import timedelta


# Grupo 1
class Comuna(models.Model):
    id_comuna = models.CharField(max_length=9, primary_key=True)
    comuna = models.CharField(max_length=40)

# Grupo 2
class Direcciones(models.Model):
    calle_dire = models.CharField(max_length=100)
    numeracio_dire = models.IntegerField()
    detalle_recep = models.CharField(max_length=400, blank=True, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='direcciones')

class Usuarios(AbstractUser):
    id_cuenta = models.AutoField(primary_key=True)
    rut_cli = models.CharField(max_length=12, unique=True)
    nombre_cli = models.CharField(max_length=25)
    apellido_cli = models.CharField(max_length=25)
    direcciones = models.ForeignKey(Direcciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Paquetes(models.Model):
    id_paquete = models.AutoField(primary_key=True)
    cuenta = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='paquetes')
    nom_paq = models.CharField(max_length=50)
    nom_recep = models.CharField(max_length=50, blank=False, null=False)
    cel_recep = models.BigIntegerField(blank=False, null=False)
    direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE)
    fec_reti = models.DateField()
    detalles_paq = models.CharField(max_length=300, null=True, blank=True)


# Grupo 4
class PlanillaRetiros(models.Model):
    id_reti = models.CharField(max_length=10, primary_key=True)
    remitente = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='retiros_remitidos')
    producto = models.ForeignKey(Paquetes, on_delete=models.CASCADE, related_name='retiros')
    

class PlanillasEntregas(models.Model):
    id_entregas = models.CharField(max_length=10, primary_key=True)
    fech_entrega = models.DateField()
    producto = models.ForeignKey(Paquetes, on_delete=models.CASCADE, related_name='entregas')
    

