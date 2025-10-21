print("=== EJERCICIO: RELACIÓN HABITACIONES-HOTEL ===\n")

# 1. Crear la clase Hotel con los atributos: id, nombre, direccion, estrellas
class Hotel:
    def __init__(self, id, nombre, direccion, estrellas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.estrellas = estrellas
        self.habitaciones = []  # Lista para almacenar las habitaciones asociadas


# 2. Crear la clase Habitacion con los atributos: id, numero, tipo, precio, hotel
class Habitacion:
    def __init__(self, id, numero, tipo, precio, hotel):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.hotel = hotel  # Relación many-to-one: muchas habitaciones pertenecen a un hotel
        hotel.habitaciones.append(self)  # Agregar la habitación al hotel automáticamente


print("=== CREANDO OBJETOS ===")

# 3. Crear un hotel con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4
hotel = Hotel(1, "Hotel Carbonero", "Plaza Parus Mayor 123", 4)

# 4. Crear tres habitaciones:
habitacion1 = Habitacion(1, 101, "Individual", 80, hotel)
habitacion2 = Habitacion(2, 102, "Doble", 120, hotel)
habitacion3 = Habitacion(3, 103, "Suite", 200, hotel)

print("=== VERIFICANDO RELACIÓN ===")

# 5. Imprimir información del hotel y sus habitaciones
print(f"Hotel: {hotel.nombre} ({hotel.estrellas} estrellas)")
print(f"Dirección: {hotel.direccion}")
print("\nHabitaciones disponibles:")
for h in hotel.habitaciones:
    print(f" - Habitación {h.numero} ({h.tipo}) - Precio: ${h.precio}")

print("\n=== RESULTADO FINAL ===")

# 7. Mostrar un mensaje confirmando la relación many-to-one
if all(h.hotel == hotel for h in hotel.habitaciones):
    print("✅ Relación many-to-one establecida correctamente entre Hotel y Habitaciones.")
else:
    print("❌ Error: la relación no se estableció correctamente.")