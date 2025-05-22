from django.contrib import admin
from .models import Producto, Categoria, Proveedor, Cliente, Venta, DetalleVenta, MovimientoInventario

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(MovimientoInventario)
