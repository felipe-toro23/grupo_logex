from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("Crear_cuenta", views.Crear_cuenta, name="Crear_cuenta"),
    path("accounts/profile/", views.profile, name="profile"),
    path("accounts/new_encomiendas/", views.guardar_paquete, name="new_encomiendas"),
    path("accounts/encomiendas/", views.encomiendas, name="encomiendas"),
    path("entregasupuser", views.entregasupuser, name="entregasupuser"),
    path("verclientes", views.verclientes, name="verclientes"),
    path('eliminar_cliente/<int:id_cliente>/', views.eliminar_cliente, name='eliminar_cliente'),
    path("salir", views.salir, name="salir")
]
