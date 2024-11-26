# nuevoConcesionario
Proyecto Servidor

# Usuario Admin
Usuario= oscaromero31
Password= oscar

# Levantar Proyecto ya empezado
python3 -m venv myvenv -> Creamos el entorno
source myvenv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate -> Creamos base de datos
python manage.py runserver -> Lanzamos el servidor

# Modelos:

1. Cliente
Representa a los clientes del concesionario:

Atributos principales: nombre completo, email (único), fecha de registro (automática) y un indicador de si es cliente VIP.
Relación: Tiene una relación OneToOne con el modelo PerfilCliente para almacenar información adicional.
2. PerfilCliente
Proporciona detalles adicionales sobre un cliente:

Relación: Cada cliente tiene un único perfil asociado (OneToOne).
Atributos adicionales: fecha de nacimiento, dirección, y teléfono.
3. Fabricante
Define los fabricantes de los vehículos:

Atributos principales: nombre (único), país de origen y año de fundación.
4. Vehículo
Representa los vehículos disponibles en el concesionario:

Relación: Cada vehículo está asociado a un único fabricante (ManyToOne).
Atributos principales: modelo, año de fabricación, precio, y un indicador de disponibilidad.
5. Compra
Registra las compras realizadas por los clientes:

Relaciones: Asocia un cliente con un vehículo (ManyToOne en ambos casos).
Atributos adicionales: fecha de compra (automática) y el precio final.
6. Concesionario
Representa los concesionarios:

Atributos principales: nombre (único), ubicación, y capacidad máxima.
7. Empleado
Define los empleados que trabajan en un concesionario:

Relación: Cada empleado pertenece a un concesionario (ManyToOne).
Atributos principales: nombre completo, cargo (con opciones predefinidas como gerente, vendedor o mecánico), y fecha de contratación.
8. Accesorio
Representa accesorios que pueden estar disponibles para los vehículos:

Relación: Los accesorios están relacionados con múltiples vehículos mediante una tabla intermedia (VehiculoAccesorio).
Atributos principales: nombre y precio.
9. VehiculoAccesorio (Tabla Intermedia)
Establece la relación ManyToMany entre vehículos y accesorios con información adicional:

Relaciones: Conecta un vehículo y un accesorio.
Atributos adicionales: fecha de instalación y coste de instalación.


