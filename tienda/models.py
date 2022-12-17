from django.db import models

# Create your models here.

class Facturacion(models.Model):
    id_factura = models.BigAutoField(primary_key = True)
    fecha = models.DateTimeField()
    tipoDeTransaccion = models.CharField(max_length = 15)
    total = models.DecimalField(max_digits = 65, decimal_places = 2)

    def __str__(self):
        return f"ID_Factura: {self.id_factura}  --  {self.tipoDeTransaccion}"


class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key = True)
    nombre_producto = models.CharField(max_length = 100)
    categoria = models.CharField(max_length = 20, )
    precio_unitario = models.DecimalField(max_digits=65,decimal_places=2)
    stock = models.BigIntegerField()

    def __str__(self):
        return f" ID: {self.id_producto} - {self.nombre_producto} - {self.categoria} - {self.precio_unitario} - {self.stock} //"


class DetalleFactura(models.Model):
    id_destallefactura = models.BigAutoField(primary_key=True)
    id_factura = models.ForeignKey(Facturacion,on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField()
    precio_unitario = models.DecimalField(max_digits = 65, decimal_places = 2)
    subtotal = models.DecimalField(max_digits=65,decimal_places=2)

    def __str__(self):
        return f"id_destallefactura: {self.id_destallefactura} -- {self.id_factura}"

