from django import forms
from .models import Producto, Facturacion

lista_productos = Producto.objects.all()
productos = []
for producto in lista_productos:
    tupla = (producto.id_producto, producto.nombre_producto)
    productos.append(tupla)

class CrearNuevoProducto(forms.Form):
    # id_producto = forms.IntegerField(label="Codigo:")
    nombre_producto = forms.CharField(label="Nombre:", max_length=200)
    categoria = forms.CharField(label="Categoria:", max_length=200)
    precio_unitario = forms.DecimalField(label="Precio individual:" , max_digits=65,decimal_places=2)
    # fecha_vencimiento = forms.DateField(label="Fecha de vencimiento:")
    stock = forms.IntegerField(label="Cantidad:")

class CrearVentaDetalle(forms.Form):
    id_producto = forms.ChoiceField(label="Producto:" ,choices=productos)
    cantidad = forms.IntegerField(label="Cantidad:")
