from django.shortcuts import render, get_object_or_404
from .models import Cliente, PerfilCliente, Fabricante, Vehiculo, Compra, Concesionario, Empleado, Accesorio

def index(request):
    return render(request, 'index.html')

# Lista de clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# Detalle de un cliente
def detalle_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    perfil = getattr(cliente, 'perfilcliente', None)  # Relación OneToOne
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente, 'perfil': perfil})

# Lista de fabricantes
def lista_fabricantes(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'fabricantes/lista_fabricantes.html', {'fabricantes': fabricantes})

# Lista de vehículos
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.select_related('fabricante').all()
    return render(request, 'vehiculos/lista_vehiculos.html', {'vehiculos': vehiculos})

# Detalle de un vehículo
def detalle_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    accesorios = vehiculo.accesorio_set.all()  # Relación ManyToMany
    return render(request, 'vehiculos/detalle_vehiculo.html', {'vehiculo': vehiculo, 'accesorios': accesorios})

# Lista de compras
def lista_compras(request):
    compras = Compra.objects.select_related('cliente', 'vehiculo').all()
    return render(request, 'compras/lista_compras.html', {'compras': compras})

# Detalle de una compra
def detalle_compra(request, id):
    compra = get_object_or_404(Compra, id=id)
    return render(request, 'compras/detalle_compra.html', {'compra': compra})

# Lista de empleados
def lista_empleados(request):
    empleados = Empleado.objects.select_related('concesionario').all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})

# Lista de concesionarios
def lista_concesionarios(request):
    concesionarios = Concesionario.objects.all()
    return render(request, 'concesionarios/lista_concesionarios.html', {'concesionarios': concesionarios})

# Lista de accesorios
def lista_accesorios(request):
    accesorios = Accesorio.objects.prefetch_related('vehiculos').all()
    return render(request, 'accesorios/lista_accesorios.html', {'accesorios': accesorios})

# Errores

# Vista para manejar errores 400
def error_400_view(request, exception):
    return render(request, 'errores/400.html', status=400)

# Vista para manejar errores 403
def error_403_view(request, exception):
    return render(request, 'errores/403.html', status=403)

# Vista para manejar errores 404
def error_404_view(request, exception):
    return render(request, 'errores/404.html', status=404)

# Vista para manejar errores 500
def error_500_view(request):
    return render(request, 'errores/500.html', status=500)