from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:id>/', views.detalle_cliente, name='detalle_cliente'),
    path('fabricantes/', views.lista_fabricantes, name='lista_fabricantes'),
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/<int:id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('compras/', views.lista_compras, name='lista_compras'),
    path('compras/<int:id>/', views.detalle_compra, name='detalle_compra'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('concesionarios/', views.lista_concesionarios, name='lista_concesionarios'),
    path('accesorios/', views.lista_accesorios, name='lista_accesorios'),
]

handler400 = 'concesionario.views.error_400_view'
handler403 = 'concesionario.views.error_403_view'
handler404 = 'concesionario.views.error_404_view'
handler500 = 'concesionario.views.error_500_view'
