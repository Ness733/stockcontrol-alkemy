from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista_productos.html", {"productos": productos})


@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "lista_proveedores.html", {"proveedores": proveedores})


@login_required
def agregar_proveedor(request):
    nuevo_proveedor = None
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            nuevo_proveedor = form.save(commit=True)
            messages.success(
                request, f"Se agrego el proveedor {nuevo_proveedor} con exito"
            )
            return redirect("agregar-proveedor")
    form = ProveedorForm()
    return render(request, "agregar_proveedores.html", {"form": form})


@login_required
def agregar_producto(request):
    nuevo_producto = None
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.save(commit=True)
            messages.success(
                request, f"Se agrego el producto {nuevo_producto} con exito"
            )
            return redirect("agregar-producto")
    form = ProductoForm()
    return render(request, "agregar_productos.html", {"form": form})
