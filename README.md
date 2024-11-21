# nuevoConcesionario
Proyecto Servidor

# Usuario Admin
Usuario= oscaromero31
Password= oscar

# Explicacion models.py

    1. Cliente
    Este modelo representa a los clientes que compran vehículos en el concesionario.

    Campos:

    nombre_completo: Guarda el nombre completo del cliente. Es un CharField con un máximo de 100 caracteres.
    email: Representa el correo electrónico del cliente. Es único, lo que asegura que no haya dos clientes con el mismo correo.
    fecha_registro: Almacena la fecha en la que el cliente se registró. Se genera automáticamente al crear un cliente.
    es_vip: Indica si el cliente es VIP o no. Por defecto es False.
    Relaciones:

    Tiene una relación OneToOne con PerfilCliente, que guarda información adicional del cliente.
    Uso: Este modelo es el punto de partida para cualquier cliente en el sistema.

    2. PerfilCliente
    Este modelo extiende la información del cliente con más detalles.

    Campos:

    cliente: Relación OneToOne con el modelo Cliente. Si se elimina un cliente, su perfil también será eliminado (on_delete=models.CASCADE).
    fecha_nacimiento: Fecha de nacimiento del cliente.
    direccion: Dirección completa del cliente. Se guarda como texto, ya que puede ser más largo.
    telefono: Número de contacto del cliente.
    Relaciones:

    Relación directa con Cliente.
    Uso: Este modelo permite almacenar información más personalizada sobre los clientes.

    3. Fabricante
    Representa las marcas o fabricantes de los vehículos vendidos.

    Campos:

    nombre: Nombre del fabricante, único para evitar duplicados.
    pais_origen: País donde se encuentra el fabricante.
    ano_fundacion: Año en el que se fundó la empresa.
    Relaciones:

    Relación ManyToOne con Vehiculo. Un fabricante puede tener múltiples vehículos.
    Uso: Este modelo organiza los fabricantes y permite identificar de dónde proviene cada vehículo.

    4. Vehiculo
    Este modelo almacena información sobre los vehículos que el concesionario tiene en venta.

    Campos:

    fabricante: Relación ManyToOne con Fabricante. Un fabricante puede tener varios vehículos, pero un vehículo pertenece a un solo fabricante.
    modelo: Nombre o modelo del vehículo.
    ano_fabricacion: Año en el que se fabricó el vehículo.
    precio: Precio del vehículo. Es un DecimalField para manejar valores monetarios.
    disponible: Indica si el vehículo está disponible para la venta.
    Relaciones:

    Relación con Fabricante y Compra.
    Uso: Este es uno de los modelos principales, ya que contiene los datos de los productos que el concesionario ofrece.

    5. Compra
    Representa las transacciones realizadas en el concesionario.

    Campos:

    cliente: Relación ManyToOne con Cliente. Un cliente puede hacer múltiples compras, pero cada compra pertenece a un solo cliente.
    vehiculo: Relación ManyToOne con Vehiculo. Un vehículo puede estar en varias compras si es un vehículo usado (en este caso, normalmente será único por transacción).
    fecha_compra: Fecha en la que se realizó la compra. Se guarda automáticamente.
    precio_final: Precio total pagado por el cliente.
    Relaciones:

    Relación entre clientes y vehículos.
    Uso: Este modelo rastrea las compras realizadas, vinculando a los clientes con los vehículos adquiridos.

    6. Concesionario
    Representa cada local o sucursal del concesionario.

    Campos:

    nombre: Nombre del concesionario, único.
    ubicacion: Dirección o ubicación del concesionario.
    capacidad_maxima: Cantidad máxima de vehículos que puede almacenar el concesionario.
    Relaciones:

    Relación con Empleado.
    Uso: Este modelo organiza los distintos concesionarios físicos o sucursales.

    7. Empleado
    Almacena información de los empleados que trabajan en el concesionario.

    Campos:

    concesionario: Relación ManyToOne con Concesionario. Un concesionario puede tener múltiples empleados, pero cada empleado pertenece a un solo concesionario.
    nombre_completo: Nombre completo del empleado.
    cargo: Rol que desempeña en el concesionario (por ejemplo, gerente, vendedor, mecánico).
    fecha_contratacion: Fecha en la que el empleado fue contratado.
    Relaciones:

    Relación con Concesionario.
    Uso: Este modelo permite gestionar a los empleados del concesionario.

    8. Accesorio
    Representa los accesorios que pueden comprarse junto con los vehículos.

    Campos:

    nombre: Nombre del accesorio (ejemplo: alfombrillas, radio, spoiler).
    precio: Precio del accesorio.
    vehiculos: Relación ManyToMany con Vehiculo a través del modelo VehiculoAccesorio.
    Relaciones:

    Relación ManyToMany con vehículos.
    Uso: Este modelo organiza los accesorios disponibles para personalizar los vehículos.

    9. VehiculoAccesorio (Tabla intermedia)
    Es una tabla que conecta vehículos con accesorios y añade información adicional.

    Campos:

    vehiculo: Relación ManyToOne con Vehiculo.
    accesorio: Relación ManyToOne con Accesorio.
    fecha_instalacion: Fecha en la que se instaló el accesorio.
    coste_instalacion: Coste adicional por instalar el accesorio.
    Relaciones:

    Une vehículos y accesorios con detalles específicos.
    Uso: Este modelo añade información extra a la relación ManyToMany entre vehículos y accesorios.

    Resumen de Relaciones
    OneToOne:

    Cliente ↔ PerfilCliente.
    ManyToOne:

    Vehiculo ↔ Fabricante.
    Compra ↔ Cliente.
    Compra ↔ Vehiculo.
    Empleado ↔ Concesionario.
    ManyToMany:

    Vehiculo ↔ Accesorio (a través de VehiculoAccesorio).




