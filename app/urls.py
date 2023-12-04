from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("Crear_cuenta", views.Crear_cuenta, name="Crear_cuenta"),
    path("accounts/profile/", views.profile, name="profile"),
    path("accounts/new_encomiendas/", views.guardar_paquete, name="new_encomiendas"),
    path("accounts/encomiendas/", views.encomiendas, name="encomiendas"),
    path("salir", views.salir, name="salir")
]
