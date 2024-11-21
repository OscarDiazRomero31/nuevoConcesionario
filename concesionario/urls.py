from django.urls import path
from . import views
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Página de índice
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),  # Lista de clientes
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),  # Detalle de cliente
    path('fabricantes/', views.FabricanteListView.as_view(), name='fabricantes'),  # Lista de fabricantes
    path('fabricante/<int:pk>/', views.FabricanteDetailView.as_view(), name='fabricante_detail'),  # Detalle de fabricante
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculos'),  # Lista de vehículos
    path('vehiculo/<int:pk>/', views.VehiculoDetailView.as_view(), name='vehiculo_detail'),  # Detalle de vehículo
    path('compras/', views.CompraListView.as_view(), name='compras'),  # Lista de compras
    path('compra/<int:pk>/', views.CompraDetailView.as_view(), name='compra_detail'),  # Detalle de compra
    path('error_demo/', views.error_demo, name='error_demo'),  # Demo de errores
]

# Configuración de handlers de error personalizados
handler404 = 'myapp.views.error_404_view'
handler500 = 'myapp.views.error_500_view'
handler403 = 'myapp.views.error_403_view'
handler400 = 'myapp.views.error_400_view'


