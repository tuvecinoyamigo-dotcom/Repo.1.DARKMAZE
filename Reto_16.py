print("=== EJERCICIO: RELACIÓN EMPLEADO-TARJETA CORPORATIVA ===\n")

# 1. Crear la clase Empleado con los atributos: id, nombre, cargo, salario
# El atributo 'tarjeta' debe inicializarse como None
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.tarjeta = None  # Relación uno a uno (inicialmente sin tarjeta)

# 2. Crear la clase TarjetaCorporativa con los atributos: id, numero, fecha_emision, empleado_id
class TarjetaCorporativa:
    def __init__(self, id, numero, fecha_emision, empleado_id):
        self.id = id
        self.numero = numero
        self.fecha_emision = fecha_emision
        self.empleado_id = empleado_id
        self.empleado = None  # Relación inversa al empleado


print("=== CREANDO OBJETOS ===")

# 3. Crear un empleado con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 45000
empleado = Empleado(1, "Alba Motacilla", "Desarrolladora", 45000)

# 4. Crear una tarjeta corporativa con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
tarjeta = TarjetaCorporativa(1, "TC001", "2025-01-15", 1)


print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Asignar la tarjeta al empleado (relación one-to-one)
empleado.tarjeta = tarjeta
tarjeta.empleado = empleado


print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del empleado y su tarjeta
print(f"Empleado: {empleado.nombre}")
print(f"Número de tarjeta: {empleado.tarjeta.numero}")
print(f"Fecha de emisión: {empleado.tarjeta.fecha_emision}")
print(f"El ID del empleado asociado a la tarjeta es: {tarjeta.empleado_id}")
print(f"La tarjeta pertenece a: {tarjeta.empleado.nombre}")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-one
if empleado.tarjeta and tarjeta.empleado == empleado:
    print("✅ Relación one-to-one establecida correctamente entre Empleado y Tarjeta Corporativa.")
else:
    print("❌ Error: la relación no se estableció correctamente.")