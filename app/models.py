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

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='usuarios_set_custom',  # Cambia este nombre
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='usuarios_set_custom',  # Cambia este nombre
        related_query_name='user',
    )

    def __str__(self):
        return self.username

class Paquetes(models.Model):
    id_paquete = models.AutoField(primary_key=True)
    cuenta = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='paquetes')
    nom_paq = models.CharField(max_length=50)
    nom_recep = models.CharField(max_length=50, blank=False, null=False)
    remitente = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='paquetes_remitidos')
    cel_recep = models.BigIntegerField(blank=False, null=False)
    direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE, related_name='paquetes_direccion', blank=False, null=False)
    fec_reti = models.DateField()
    detalles_paq = models.CharField(max_length=300, null=True, blank=True)

   
    def save(self, commit=True, request=None):
        paquete = super().save(commit=False)

        # Obtén el remitente desde el usuario actual
        remitente = request.user
        paquete.remitente = remitente

        if commit:
            paquete.save()

            # Crear una nueva dirección y enlazarla al paquete como dirección de entrega
            nueva_direccion = Direcciones.objects.create(
                calle=self.cleaned_data['direccion_calle'],
                numeracion=self.cleaned_data['direccion_numeracion'],
                comuna=self.cleaned_data['direccion_comuna'],
                # Otros campos de dirección...
            )
            paquete.direccion = nueva_direccion
            paquete.save()

        return paquete

# Grupo 4
class PlanillaRetiros(models.Model):
    id_reti = models.CharField(max_length=10, primary_key=True)
    remitente = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='retiros_remitidos')
    producto = models.ForeignKey(Paquetes, on_delete=models.CASCADE, related_name='retiros')
    

class PlanillasEntregas(models.Model):
    id_entregas = models.CharField(max_length=10, primary_key=True)
    fech_entrega = models.DateField()
    producto = models.ForeignKey(Paquetes, on_delete=models.CASCADE, related_name='entregas')
    

@receiver(pre_save, sender=PlanillasEntregas)
def calcular_fecha_entrega(sender, instance, **kwargs):
    # Verificar si la fecha de entrega ya está establecida
    if not instance.fech_entrega:
        # Calcular la fecha de entrega como 2 días después de la fecha de registro
        fecha_registro = PlanillaRetiros.objects.get(producto=instance.producto).fecha_registro
        fecha_entrega = fecha_registro + timedelta(days=2)
        
        # Establecer la fecha de entrega en el modelo PlanillasEntregas
        instance.fech_entrega = fecha_entrega