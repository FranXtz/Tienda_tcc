from django.shortcuts import render, redirect
from django.http import HttpResponse
import ast
import datetime
from .models import Producto, Facturacion, DetalleFactura   
from .forms import CrearNuevoProducto, CrearVentaDetalle
# Create your views here.

def index(request):
    return render(request, 'index.html')

def inventario(request):
    productos = Producto.objects.all()
    return render(request, 'inventario.html', {
        'productos':productos
    })

def compra(request):
    compras = Facturacion.objects.filter(tipoDeTransaccion='COMPRA')
    return render(request, 'compras/compra.html', {
        'compras':compras,
        'tipo':'COMPRA'
    })

def venta(request):
    ventas = Facturacion.objects.filter(tipoDeTransaccion='VENTA')
    return render(request, 'ventas/venta.html', {
        'ventas':ventas,
        'tipo':'VENTA'
    })

def crear_producto(request):
    if request.method == 'GET':
        return render(request, 'crear_producto.html', {
            'form':CrearNuevoProducto
        })
    else:
        Producto.objects.create(nombre_producto=request.POST['nombre_producto'], categoria=request.POST['categoria'], precio_unitario=request.POST['precio_unitario'], fecha_vencimiento=None, stock=request.POST['stock'])
        return redirect('inventario')

def detalle_venta(request, id):
    detalle = DetalleFactura.objects.filter(id_factura=id)
    print(detalle)
    return render(request, 'ventas/detalles_venta.html', {
        'detalle':detalle
    })

def detalle_compra(request, id):
    detalle = DetalleFactura.objects.filter(id_factura=id)
    print(detalle)
    return render(request, 'compras/detalles_compra.html', {
        'detalle':detalle
    })

def crear_transaccion(request, factura):
    #El parametro se recive como string por po que toca convertirlo en diccionario
    factura = ast.literal_eval(factura) 
    if request.method == 'GET':
        return render(request, 'crear_transaccion.html', {
            'form':CrearVentaDetalle,
            'factura':factura
        })
    else:
        fact = Facturacion.objects.all()
        if fact[len(fact)-1].id_factura != factura['id_factura']:
            Facturacion.objects.create(fecha=factura['fecha'], tipoDeTransaccion=factura['tipoDeTransaccion'], total=0)

        canti = request.POST['cantidad']
        id_p = request.POST['id_producto']
        producto = Producto.objects.get(id_producto=id_p)
        subt = int(canti) * int(producto.precio_unitario)
        
        # Se calcula el subtotas
        #comprobar si no existe la factura para crearla   
        instanciaFactura = Facturacion.objects.get(id_factura = factura['id_factura'])
        instanciaProducto = Producto.objects.get(id_producto =id_p )
        DetalleFactura.objects.create(id_factura=instanciaFactura, id_producto=instanciaProducto, cantidad=canti, precio_unitario=producto.precio_unitario, subtotal=subt)

        detalles = DetalleFactura.objects.filter(id_factura=factura['id_factura'])
        total = 0
        for detalle in detalles:
            subtotal = detalle.subtotal
            total += subtotal

        print(total)
        instanciaFactura.total=total
        instanciaFactura.save()

        if factura['tipoDeTransaccion'] == 'VENTA':
            instanciaProducto.stock -= int(canti)
            instanciaProducto.save()
        elif factura['tipoDeTransaccion'] == 'COMPRA':
            instanciaProducto.stock += int(canti)
            instanciaProducto.save()

        return redirect('crear_transaccion', factura)


def crear_factura(request, tipo):
    fecha= datetime.datetime.now()
    f = f"{fecha.year}-{fecha.month}-{fecha.day} {fecha.hour}:{fecha.minute}:{fecha.second}"
    fact = Facturacion.objects.all()
    longitud = len(fact)
    ultimo = fact[longitud-1]
    id_factura = int(ultimo.id_factura)+1
    factura = {"tipoDeTransaccion":tipo, "fecha":f, "id_factura":id_factura}
    return render(request, 'crear_factura.html', {
        'factura':factura
    })
                                                                                                               