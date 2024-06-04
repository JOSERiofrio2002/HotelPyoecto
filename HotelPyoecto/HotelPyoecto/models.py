from django.db import models
from django.contrib.auth.models import User
from enum import Enum

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    email = models.EmailField()

    class Meta:
        abstract = True

class Cliente(Persona):
    telefono = models.CharField(max_length=10)

    def pedirHabitacion(self):
        pass

    def darInformacion(self):
        pass

class Empleado(Persona):
    cargo = models.CharField(max_length=50)

    def asignarHabitacion(self):
        pass

    def verificarEstado(self):
        pass

class TipoHabitacion(Enum):
    SIMPLE = 'Simple'
    DOBLE = 'Doble'
    SUITE = 'Suite'

class Habitacion(models.Model):
    numero = models.IntegerField(unique=True)
    tipo = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in TipoHabitacion])
    precio = models.FloatField()
    estado = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in EstadoReserva], default=EstadoReserva.LIBRE.name)

    def verificarEstado(self):
        return self.estado

    def reservar(self):
        if self.estado == EstadoReserva.LIBRE.name:
            self.estado = EstadoReserva.RESERVADA.name
            self.save()
            return True
        return False

class EstadoReserva(Enum):
    RESERVADA = 'Reservada'
    OCUPADA = 'Ocupada'
    LIBRE = 'Libre'

class Reservacion(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    fecha_inicio = models.DateField()
    estado = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in EstadoReserva], default=EstadoReserva.RESERVADA.name)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservacionList')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def realizarReserva(self):
        if self.habitacion.reservar():
            self.estado = EstadoReserva.RESERVADA.name
            self.save()
            return True
        return False

    def cancelarReserva(self):
        self.estado = EstadoReserva.LIBRE.name
        self.habitacion.estado = EstadoReserva.LIBRE.name
        self.habitacion.save()
        self.save()

    def reagendarReserva(self, nueva_fecha):
        self.fecha_inicio = nueva_fecha
        self.save()

class Factura(models.Model):
    numeroFactura = models.CharField(max_length=10, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valorTotal = models.FloatField()
    descripcion = models.TextField()

    def generarFactura(self):
        return {
            "numero_factura": self.numeroFactura,
            "fecha": self.fecha,
            "cliente": self.cliente.nombre + " " + self.cliente.apellido,
            "valor_total": self.valorTotal,
            "descripcion": self.descripcion
        }

class Transaccion(models.Model):
    idTransaccion = models.CharField(max_length=10, unique=True)
    fechaTransaccion = models.DateField()
    monto = models.FloatField()
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

    def procesarTransaccion(self, metodoPago):
        return metodoPago.realizarPago()

class Pago(models.Model):
    class Meta:
        abstract = True

    def procesarPago(self):
        pass

class PagoTarjeta(Pago):
    numeroTarjeta = models.CharField(max_length=16)
    nombreDueño = models.CharField(max_length=50)
    fechaExpiracion = models.DateField()

    def realizarPago(self):
        return "Pago con tarjeta realizado"

class PagoEfectivo(Pago):
    def realizarPago(self):
        return "Pago en efectivo realizado"

class CheckIn(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def realizarCheckIn(self):
        if self.habitacion.estado == EstadoReserva.RESERVADA.name:
            self.habitacion.estado = EstadoReserva.OCUPADA.name
            self.habitacion.save()
            return True
        return False

class CheckOut(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def realizarCheckOut(self):
        if self.habitacion.estado == EstadoReserva.OCUPADA.name:
            self.habitacion.estado = EstadoReserva.LIBRE.name
            self.habitacion.save()
            return True
        return False
