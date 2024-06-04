from django.contrib import admin
from HotelPyoecto.models import Cliente, Empleado, Habitacion, Reservacion, Factura, Transaccion, PagoTarjeta, PagoEfectivo, CheckIn, CheckOut

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Habitacion)
admin.site.register(Reservacion)
admin.site.register(Factura)
admin.site.register(Transaccion)
admin.site.register(PagoTarjeta)
admin.site.register(PagoEfectivo)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
