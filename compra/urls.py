from django.urls import path
from .views import (
    lista_productos,
    lista_proveedores,
    agregar_producto,
    agregar_proveedor,
)

urlpatterns = [
    path("", lista_productos, name="lista_productos"),
    path("proveedores/", lista_proveedores, name="lista_proveedores"),
    path("agregar-producto/", agregar_producto, name="agregar-producto"),
    path("agregar-proveedor/", agregar_proveedor, name="agregar-proveedor"),
]
