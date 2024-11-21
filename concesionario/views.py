from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.http import Http404, HttpResponseForbidden, HttpResponseBadRequest
from .models import Cliente, Fabricante, Vehiculo, Compra

# Vista de índice
class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {'titulo': 'Bienvenido al Concesionario'}

# Vistas de clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes.html"
    context_object_name = "clientes"

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente_detail.html"

# Vistas de fabricantes
class FabricanteListView(ListView):
    model = Fabricante
    template_name = "fabricantes.html"
    context_object_name = "fabricantes"

class FabricanteDetailView(DetailView):
    model = Fabricante
    template_name = "fabricante_detail.html"

# Vistas de vehículos
class VehiculoListView(ListView):
    model = Vehiculo
    template_name = "vehiculos.html"
    context_object_name = "vehiculos"

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = "vehiculo_detail.html"

# Vistas de compras
class CompraListView(ListView):
    model = Compra
    template_name = "compras.html"
    context_object_name = "compras"

class CompraDetailView(DetailView):
    model = Compra
    template_name = "compra_detail.html"

# Vista para generar errores
def error_demo(request):
    raise Http404("Esta es una demostración del error 404.")

# Manejo de errores
def error_404_view(request, exception):
    """
    Muestra la página personalizada de error 404.
    """
    return render(request, 'errors/404.html', status=404)

def error_500_view(request):
    """
    Muestra la página personalizada de error 500.
    """
    return render(request, 'errors/500.html', status=500)

def error_403_view(request, exception):
    """
    Muestra la página personalizada de error 403.
    """
    return render(request, 'errors/403.html', status=403)

def error_400_view(request, exception):
    """
    Muestra la página personalizada de error 400.
    """
    return render(request, 'errors/400.html', status=400)
