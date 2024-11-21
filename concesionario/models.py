from django.db import models

# Modelo Cliente
class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)  # Nombre completo del cliente
    email = models.EmailField(unique=True)  # Correo electrónico único
    fecha_registro = models.DateField(auto_now_add=True)  # Fecha de registro automática
    es_vip = models.BooleanField(default=False)  # Indica si el cliente es VIP

    def __str__(self):
        return self.nombre_completo


# Modelo PerfilCliente (relación OneToOne con Cliente)
class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)  # Relación uno a uno con Cliente
    fecha_nacimiento = models.DateField(null=True, blank=True)  # Fecha de nacimiento
    direccion = models.TextField(null=True, blank=True)  # Dirección completa
    telefono = models.CharField(max_length=15, null=True, blank=True)  # Número de teléfono

    def __str__(self):
        return f"Perfil de {self.cliente.nombre_completo}"


# Modelo Fabricante
class Fabricante(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  # Nombre del fabricante
    pais_origen = models.CharField(max_length=50)  # País de origen
    ano_fundacion = models.IntegerField()  # Año de fundación

    def __str__(self):
        return self.nombre


# Modelo Vehículo
class Vehiculo(models.Model):
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)  # Relación ManyToOne con Fabricante
    modelo = models.CharField(max_length=100)  # Modelo del vehículo
    ano_fabricacion = models.IntegerField()  # Año de fabricación
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del vehículo
    disponible = models.BooleanField(default=True)  # Indica si el vehículo está disponible

    def __str__(self):
        return f"{self.modelo} - {self.fabricante.nombre}"


# Modelo Compra
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación ManyToOne con Cliente
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)  # Relación ManyToOne con Vehículo
    fecha_compra = models.DateTimeField(auto_now_add=True)  # Fecha automática de compra
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)  # Precio final de la compra

    def __str__(self):
        return f"Compra de {self.vehiculo.modelo} por {self.cliente.nombre_completo}"


# Modelo Concesionario
class Concesionario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  # Nombre único del concesionario
    ubicacion = models.CharField(max_length=100)  # Ubicación
    capacidad_maxima = models.IntegerField()  # Capacidad máxima de vehículos

    def __str__(self):
        return self.nombre


# Modelo Empleado
class Empleado(models.Model):
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE)  # Relación ManyToOne con Concesionario
    nombre_completo = models.CharField(max_length=100)  # Nombre del empleado
    cargo = models.CharField(
        max_length=50,
        choices=[("Gerente", "Gerente"), ("Vendedor", "Vendedor"), ("Mecánico", "Mecánico")],
        default="Vendedor"
    )  # Cargo que ocupa
    fecha_contratacion = models.DateField(null=True, blank=True)  # Fecha de contratación

    def __str__(self):
        return f"{self.nombre_completo} - {self.cargo}"


# Modelo Accesorio
class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del accesorio
    precio = models.DecimalField(max_digits=8, decimal_places=2)  # Precio del accesorio
    vehiculos = models.ManyToManyField('Vehiculo', through='VehiculoAccesorio')  # Relación ManyToMany con tabla intermedia

    def __str__(self):
        return self.nombre


# Modelo Vehículo-Accesorio (tabla intermedia)
class VehiculoAccesorio(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)  # Relación ManyToOne con Vehículo
    accesorio = models.ForeignKey(Accesorio, on_delete=models.CASCADE)  # Relación ManyToOne con Accesorio
    fecha_instalacion = models.DateField(null=True, blank=True)  # Fecha de instalación del accesorio
    coste_instalacion = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)  # Coste de instalación

    def __str__(self):
        return f"{self.accesorio.nombre} en {self.vehiculo.modelo}"
