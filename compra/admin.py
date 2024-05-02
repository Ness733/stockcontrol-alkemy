from django.contrib import admin
from .models import Proveedor, Producto


# Register your models here.
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock_actual", "proveedor")
