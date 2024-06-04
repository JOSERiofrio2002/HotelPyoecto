
from django.contrib import admin
from django.urls import path, include
from.models import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),  # Incluye las URLs de la aplicación hotel
]

urlpatterns = [
    path('', views.index, name='index'),

    # Cliente URLs
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('cliente/create/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/<int:pk>/update/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('cliente/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente-delete'),

    # Empleado URLs
    path('empleados/', views.EmpleadoListView.as_view(), name='empleados'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('empleado/create/', views.EmpleadoCreateView.as_view(), name='empleado-create'),
    path('empleado/<int:pk>/update/', views.EmpleadoUpdateView.as_view(), name='empleado-update'),
    path('empleado/<int:pk>/delete/', views.EmpleadoDeleteView.as_view(), name='empleado-delete'),

    # Habitacion URLs
    path('habitaciones/', views.HabitacionListView.as_view(), name='habitaciones'),
    path('habitacion/<int:pk>/', views.HabitacionDetailView.as_view(), name='habitacion-detail'),
    path('habitacion/create/', views.HabitacionCreateView.as_view(), name='habitacion-create'),
    path('habitacion/<int:pk>/update/', views.HabitacionUpdateView.as_view(), name='habitacion-update'),
    path('habitacion/<int:pk>/delete/', views.HabitacionDeleteView.as_view(), name='habitacion-delete'),

    # Reservacion URLs
    path('reservaciones/', views.ReservacionListView.as_view(), name='reservaciones'),
    path('reservacion/<int:pk>/', views.ReservacionDetailView.as_view(), name='reservacion-detail'),
    path('reservacion/create/', views.ReservacionCreateView.as_view(), name='reservacion-create'),
    path('reservacion/<int:pk>/update/', views.ReservacionUpdateView.as_view(), name='reservacion-update'),
    path('reservacion/<int:pk>/delete/', views.ReservacionDeleteView.as_view(), name='reservacion-delete'),

    # Factura URLs
    path('facturas/', views.FacturaListView.as_view(), name='facturas'),
    path('factura/<int:pk>/', views.FacturaDetailView.as_view(), name='factura-detail'),
    path('factura/create/', views.FacturaCreateView.as_view(), name='factura-create'),
    path('factura/<int:pk>/update/', views.FacturaUpdateView.as_view(), name='factura-update'),
    path('factura/<int:pk>/delete/', views.FacturaDeleteView.as_view(), name='factura-delete'),

    # CheckIn URLs
    path('checkins/', views.CheckInListView.as_view(), name='checkins'),
    path('checkin/<int:pk>/', views.CheckInDetailView.as_view(), name='checkin-detail'),
    path('checkin/create/', views.CheckInCreateView.as_view(), name='checkin-create'),
    path('checkin/<int:pk>/update/', views.CheckInUpdateView.as_view(), name='checkin-update'),
    path('checkin/<int:pk>/delete/', views.CheckInDeleteView.as_view(), name='checkin-delete'),

    # CheckOut URLs
    path('checkouts/', views.CheckOutListView.as_view(), name='checkouts'),
    path('checkout/<int:pk>/', views.CheckOutDetailView.as_view(), name='checkout-detail'),
    path('checkout/create/', views.CheckOutCreateView.as_view(), name='checkout-create'),
    path('checkout/<int:pk>/update/', views.CheckOutUpdateView.as_view(), name='checkout-update'),
    path('checkout/<int:pk>/delete/', views.CheckOutDeleteView.as_view(), name='checkout-delete'),
]
