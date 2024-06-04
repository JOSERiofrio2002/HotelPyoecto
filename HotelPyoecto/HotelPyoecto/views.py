from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Cliente, Empleado, Habitacion, Reservacion, Factura, CheckIn, CheckOut

def index(request):
    num_clientes = Cliente.objects.count()
    num_habitaciones = Habitacion.objects.count()
    num_reservaciones = Reservacion.objects.count()
    num_empleados = Empleado.objects.count()

    context = {
        'num_clientes': num_clientes,
        'num_habitaciones': num_habitaciones,
        'num_reservaciones': num_reservaciones,
        'num_empleados': num_empleados,
    }

    return render(request, 'hotel/index.html', context=context)

# Vistas para Cliente
class ClienteListView(generic.ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'hotel/cliente_list.html'

class ClienteDetailView(generic.DetailView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'hotel/cliente_detail.html'

class ClienteCreateView(generic.CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('clientes')

class ClienteUpdateView(generic.UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('clientes')

class ClienteDeleteView(generic.DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')

# Vistas para Empleado
class EmpleadoListView(generic.ListView):
    model = Empleado
    context_object_name = 'empleados'
    template_name = 'hotel/empleado_list.html'

class EmpleadoDetailView(generic.DetailView):
    model = Empleado
    context_object_name = 'empleado'
    template_name = 'hotel/empleado_detail.html'

class EmpleadoCreateView(generic.CreateView):
    model = Empleado
    fields = '__all__'
    success_url = reverse_lazy('empleados')

class EmpleadoUpdateView(generic.UpdateView):
    model = Empleado
    fields = '__all__'
    success_url = reverse_lazy('empleados')

class EmpleadoDeleteView(generic.DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

# Vistas para Habitacion
class HabitacionListView(generic.ListView):
    model = Habitacion
    context_object_name = 'habitaciones'
    template_name = 'hotel/habitacion_list.html'

class HabitacionDetailView(generic.DetailView):
    model = Habitacion
    context_object_name = 'habitacion'
    template_name = 'hotel/habitacion_detail.html'

class HabitacionCreateView(generic.CreateView):
    model = Habitacion
    fields = '__all__'
    success_url = reverse_lazy('habitaciones')

class HabitacionUpdateView(generic.UpdateView):
    model = Habitacion
    fields = '__all__'
    success_url = reverse_lazy('habitaciones')

class HabitacionDeleteView(generic.DeleteView):
    model = Habitacion
    success_url = reverse_lazy('habitaciones')

# Vistas para Reservacion
class ReservacionListView(generic.ListView):
    model = Reservacion
    context_object_name = 'reservaciones'
    template_name = 'hotel/reservacion_list.html'

class ReservacionDetailView(generic.DetailView):
    model = Reservacion
    context_object_name = 'reservacion'
    template_name = 'hotel/reservacion_detail.html'

class ReservacionCreateView(generic.CreateView):
    model = Reservacion
    fields = '__all__'
    success_url = reverse_lazy('reservaciones')

class ReservacionUpdateView(generic.UpdateView):
    model = Reservacion
    fields = '__all__'
    success_url = reverse_lazy('reservaciones')

class ReservacionDeleteView(generic.DeleteView):
    model = Reservacion
    success_url = reverse_lazy('reservaciones')

# Vistas para Factura
class FacturaListView(generic.ListView):
    model = Factura
    context_object_name = 'facturas'
    template_name = 'hotel/factura_list.html'

class FacturaDetailView(generic.DetailView):
    model = Factura
    context_object_name = 'factura'
    template_name = 'hotel/factura_detail.html'

class FacturaCreateView(generic.CreateView):
    model = Factura
    fields = '__all__'
    success_url = reverse_lazy('facturas')

class FacturaUpdateView(generic.UpdateView):
    model = Factura
    fields = '__all__'
    success_url = reverse_lazy('facturas')

class FacturaDeleteView(generic.DeleteView):
    model = Factura
    success_url = reverse_lazy('facturas')

# Vistas para CheckIn
class CheckInListView(generic.ListView):
    model = CheckIn
    context_object_name = 'checkins'
    template_name = 'hotel/checkin_list.html'

class CheckInDetailView(generic.DetailView):
    model = CheckIn
    context_object_name = 'checkin'
    template_name = 'hotel/checkin_detail.html'

class CheckInCreateView(generic.CreateView):
    model = CheckIn
    fields = '__all__'
    success_url = reverse_lazy('checkins')

class CheckInUpdateView(generic.UpdateView):
    model = CheckIn
    fields = '__all__'
    success_url = reverse_lazy('checkins')

class CheckInDeleteView(generic.DeleteView):
    model = CheckIn
    success_url = reverse_lazy('checkins')

# Vistas para CheckOut
class CheckOutListView(generic.ListView):
    model = CheckOut
    context_object_name = 'checkouts'
    template_name = 'hotel/checkout_list.html'

class CheckOutDetailView(generic.DetailView):
    model = CheckOut
    context_object_name = 'checkout'
    template_name = 'hotel/checkout_detail.html'

class CheckOutCreateView(generic.CreateView):
    model = CheckOut
    fields = '__all__'
    success_url = reverse_lazy('checkouts')

class CheckOutUpdateView(generic.UpdateView):
    model = CheckOut
    fields = '__all__'
    success_url = reverse_lazy('checkouts')

class CheckOutDeleteView(generic.DeleteView):
    model = CheckOut
    success_url = reverse_lazy('checkouts')
