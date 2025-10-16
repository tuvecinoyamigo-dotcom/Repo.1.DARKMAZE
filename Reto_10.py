print("=== PROGRAMA: GESTIÓN DE CALIFICACIONES ===\n")

# Estructura inicial del diccionario
estudiantes = {
    "Ana": [8, 9, 7],
    "Carlos": [6, 8, 9],
    "Elena": [9, 9, 8]
}

print("=== DICCIONARIO INICIAL ===")
print("Estudiantes y sus calificaciones:")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificaciones}")

print("\n=== OPERACIÓN 1: AÑADIR NUEVO ESTUDIANTE ===")
# 1. Añade un nuevo estudiante con sus calificaciones al diccionario
estudiantes["Marcos"] = [10, 9, 10]

print("Diccionario actualizado:")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificaciones}")

print("\n=== OPERACIÓN 2: CALCULAR PROMEDIOS ===")
# 2. Calcula y muestra el promedio de calificaciones de cada estudiante
promedios = {}
for nombre, calificaciones in estudiantes.items():
    promedio = sum(calificaciones) / len(calificaciones)
    promedios[nombre] = promedio
    print(f"{nombre}: promedio = {promedio:.2f}")

print("\n=== OPERACIÓN 3: ENCONTRAR MEJOR ESTUDIANTE ===")
# 3. Identifica y muestra el nombre del estudiante con el promedio más alto
mejor_estudiante = max(promedios, key=promedios.get)
print(f"El mejor estudiante es {mejor_estudiante} con un promedio de {promedios[mejor_estudiante]:.2f}")