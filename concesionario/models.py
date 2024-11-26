from django.db import models

# Modelo Cliente
class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)  
    email = models.EmailField(unique=True)  
    fecha_registro = models.DateField(auto_now_add=True)  
    es_vip = models.BooleanField(default=False)  

    def __str__(self):
        return self.nombre_completo


# Modelo PerfilCliente (relación OneToOne con Cliente)
class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)  
    fecha_nacimiento = models.DateField(null=True, blank=True)  
    direccion = models.TextField(null=True, blank=True)  
    telefono = models.CharField(max_length=15, null=True, blank=True)  
    def __str__(self):
        return f"Perfil de {self.cliente.nombre_completo}"


# Modelo Fabricante
class Fabricante(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  
    pais_origen = models.CharField(max_length=50)  
    ano_fundacion = models.IntegerField()  

    def __str__(self):
        return self.nombre


# Modelo Vehículo
class Vehiculo(models.Model):
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)  
    modelo = models.CharField(max_length=100)  
    ano_fabricacion = models.IntegerField()  
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    disponible = models.BooleanField(default=True)  
    
    def __str__(self):
        return f"{self.modelo} - {self.fabricante.nombre}"


# Modelo Compra
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.vehiculo.modelo} por {self.cliente.nombre_completo}"


# Modelo Concesionario
class Concesionario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  
    ubicacion = models.CharField(max_length=100)  
    capacidad_maxima = models.IntegerField()  
    def __str__(self):
        return self.nombre


# Modelo Empleado
class Empleado(models.Model):
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE)  
    nombre_completo = models.CharField(max_length=100)  
    cargo = models.CharField(
        max_length=50,
        choices=[("Gerente", "Gerente"), ("Vendedor", "Vendedor"), ("Mecánico", "Mecánico")],
        default="Vendedor"
    )  # Cargo que ocupa
    fecha_contratacion = models.DateField(null=True, blank=True)  

    def __str__(self):
        return f"{self.nombre_completo} - {self.cargo}"


# Modelo Accesorio
class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)  
    precio = models.DecimalField(max_digits=8, decimal_places=2)  
    vehiculos = models.ManyToManyField('Vehiculo', through='VehiculoAccesorio')  

    def __str__(self):
        return self.nombre


# Modelo Vehículo-Accesorio (tabla intermedia)
class VehiculoAccesorio(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)  
    accesorio = models.ForeignKey(Accesorio, on_delete=models.CASCADE)  
    fecha_instalacion = models.DateField(null=True, blank=True)  
    coste_instalacion = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)  

    def __str__(self):
        return f"{self.accesorio.nombre} en {self.vehiculo.modelo}"
