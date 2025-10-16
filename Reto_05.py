print("=== PROGRAMA: GENERADOR DE PATRÓN TRIANGULAR ===\n")

# Solicitar al usuario la altura del triángulo
altura = input("Introduce la altura del triángulo (número entero positivo): ")
# Escribe aquí tu código para pedir el número al usuario
print()

# Convertir la entrada a número entero
altura = int(altura)
# Escribe aquí tu código para la conversión

print(f"\nGenerando patrón triangular de altura {altura}:")
print("-" * 30)

# Generar el patrón usando bucles for anidados
# Bucle externo: para cada fila (desde 1 hasta la altura)
for i in range(1, altura + 1):
    # Bucle interno: para cada número en la fila actual (desde 1 hasta el número de fila)
    for j in range(1, i + 1):
        # Imprimir cada número seguido de un espacio (sin salto de línea)
        print(j, end=" ")
    # Después de completar una fila, hacer un salto de línea
    print()

print("-" * 30)
print("Patrón completado!")