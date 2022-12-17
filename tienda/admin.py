from django.contrib import admin
from .models import Producto, Facturacion, DetalleFactura
# Register your models here.

admin.site.register(Producto)
admin.site.register(Facturacion)
admin.site.register(DetalleFactura)
