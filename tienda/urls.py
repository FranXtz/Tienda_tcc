from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('inventario/', views.inventario, name='inventario'),
    path('compras/', views.compra, name='compras'),
    path('ventas/', views.venta, name='ventas'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('crear_transaccion/<factura>', views.crear_transaccion, name='crear_transaccion'),
    path('detalle_venta/<int:id>', views.detalle_venta, name='detalle_venta'),
    path('detalle_compra/<int:id>', views.detalle_compra, name='detalle_compra'),
    path('crear_factura/<str:tipo>', views.crear_factura, name='crear_factura')
    
]
