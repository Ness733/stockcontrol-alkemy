from django.shortcuts import render, redirect
from django.urls import reverse
from compra.models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm
from django.contrib import messages


# Create your views here.


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista_productos.html", {"productos": productos})


def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "lista_proveedores.html", {"proveedores": proveedores})


def agregar_proveedor(request):
    nuevo_proveedor = None
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            nuevo_proveedor = form.save(commit=True)
            messages.success(
                request, f"Se agrego el proveedor {nuevo_proveedor} con exito"
            )
            return redirect("lista_proveedores")
    form = ProveedorForm()
    return render(request, "agregar_proveedores.html", {"form": form})


def agregar_producto(request):
    nuevo_producto = None
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.save(commit=True)
            messages.success(
                request, f"Se agrego el producto {nuevo_producto} con exito"
            )
            return redirect("lista_productos")
    form = ProductoForm()
    return render(request, "agregar_productos.html", {"form": form})
