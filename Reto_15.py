print("=== PROGRAMA: POLIMORFISMO CON VEHÍCULOS ===\n")

# Clase base Vehiculo
class Vehiculo:
    def desplazarse(self):
        # Implementar mensaje genérico de desplazamiento
        print("El vehículo se está desplazando.")

# Clase Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def desplazarse(self):
        # Sobreescribir el método para mostrar cómo se desplaza un coche
        print("El coche se desplaza por carretera.")

# Clase Barco que hereda de Vehiculo
class Barco(Vehiculo):
    def desplazarse(self):
        # Sobreescribir el método para mostrar cómo se desplaza un barco
        print("El barco navega por el mar.")

# Clase Avion que hereda de Vehiculo
class Avion(Vehiculo):
    def desplazarse(self):
        # Sobreescribir el método para mostrar cómo se desplaza un avión
        print("El avión vuela por el cielo.")

# Función que demuestra polimorfismo
def iniciar_viaje(vehiculo):
    # Llamar al método desplazarse() del vehículo recibido
    vehiculo.desplazarse()

# === CREACIÓN DE INSTANCIAS ===
print("=== CREANDO VEHÍCULOS ===")

# Crear una instancia de cada tipo de vehículo
vehiculo_generico = Vehiculo()
coche = Coche()
barco = Barco()
avion = Avion()

print("✓ Vehículos creados exitosamente")

print("\n=== DEMOSTRANDO POLIMORFISMO ===")

# Crear una lista con todos los vehículos
vehiculos = [vehiculo_generico, coche, barco, avion]

# Usar la función iniciar_viaje() con cada vehículo
for v in vehiculos:
    iniciar_viaje(v)

print("\n=== PRUEBAS INDIVIDUALES ===")

# Llamar a iniciar_viaje() con cada vehículo individualmente
iniciar_viaje(vehiculo_generico)
iniciar_viaje(coche)
iniciar_viaje(barco)
iniciar_viaje(avion)