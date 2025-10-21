print("=== EJERCICIO: RELACIÓN CARPETA-ARCHIVOS ===\n")

# 1. Crear la clase Carpeta con los atributos: id, nombre, fecha_creacion
# El atributo 'archivos' debe inicializarse como una lista vacía
class Carpeta:
    def __init__(self, id, nombre, fecha_creacion):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.archivos = []  # Relación one-to-many (una carpeta puede tener muchos archivos)


# 2. Crear la clase Archivo con los atributos: id, nombre, extension, tamaño, carpeta_id
class Archivo:
    def __init__(self, id, nombre, extension, tamaño, carpeta_id):
        self.id = id
        self.nombre = nombre
        self.extension = extension
        self.tamaño = tamaño
        self.carpeta_id = carpeta_id


print("=== CREANDO OBJETOS ===")

# 3. Crear una carpeta con id: 1, nombre: Proyecto Aviberico, fecha de creación: 2025-01-15
carpeta = Carpeta(1, "Proyecto Aviberico", "2025-01-15")

# 4. Crear tres archivos
archivo1 = Archivo(1, "main", "py", 1024, 1)
archivo2 = Archivo(2, "config", "json", 512, 1)
archivo3 = Archivo(3, "readme", "md", 256, 1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Agregar los archivos a la carpeta (relación one-to-many)
carpeta.archivos.append(archivo1)
carpeta.archivos.append(archivo2)
carpeta.archivos.append(archivo3)

print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información de la carpeta y sus archivos
print(f"Carpeta: {carpeta.nombre}")
print(f"Fecha de creación: {carpeta.fecha_creacion}")
print(f"Número total de archivos: {len(carpeta.archivos)}")

print("\nArchivos contenidos:")
for archivo in carpeta.archivos:
    print(f" - {archivo.nombre}.{archivo.extension} ({archivo.tamaño} KB)")

print("\n=== RESULTADO FINAL ===")

# 7. Mostrar un mensaje confirmando la relación one-to-many
if len(carpeta.archivos) > 0 and all(a.carpeta_id == carpeta.id for a in carpeta.archivos):
    print("V Relación one-to-many establecida correctamente entre Carpeta y Archivos.")
else:
    print("X Error: la relación no se estableció correctamente.")