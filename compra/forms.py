from django import forms

from compra.models import Proveedor, Producto


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "apellido", "dni"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control input-sm"}),
            "apellido": forms.TextInput(attrs={"class": "form-control input-sm"}),
            "dni": forms.TextInput(attrs={"class": "form-control input-sm"}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "stock_actual", "proveedor"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control input-sm"}),
            "precio": forms.TextInput(attrs={"class": "form-control input-sm"}),
            "stock_actual": forms.TextInput(attrs={"class": "form-control input-sm"}),
            "proveedor": forms.Select(attrs={"class": "form-control input-sm"}),
        }
