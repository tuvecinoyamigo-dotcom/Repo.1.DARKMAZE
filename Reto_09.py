print("=== PROGRAMA: INFORMACIÓN DE PRODUCTO ===\n")

# Crear una tupla llamada 'producto' con: nombre, precio y disponibilidad
producto = ("Teclado mecánico", 59.99, True)
# Escribe aquí tu código

print("=== OPERACIÓN 1: VERIFICAR TIPO DE DATO ===")
# 1. Imprime el tipo de dato de la variable 'producto'
print(type(producto))
# Escribe aquí tu código

print("\n=== OPERACIÓN 2: ACCEDER AL NOMBRE ===")
# 2. Accede e imprime el nombre del producto (primer elemento)
print(producto[0])
# Escribe aquí tu código

print("\n=== OPERACIÓN 3: ACCEDER AL PRECIO ===")
# 3. Accede e imprime el precio (segundo elemento)
print(producto[1])
# Escribe aquí tu código

print("\n=== OPERACIÓN 4: DESEMPAQUETADO DE TUPLA ===")
# 4. Utiliza el desempaquetado para asignar cada valor a variables separadas
nombre, precio, disponible = producto
# Escribe aquí tu código

print(f"Variables desempaquetadas:")
print(f"nombre: {nombre}")
print(f"precio: {precio}")
print(f"disponible: {disponible}")

print("\n=== OPERACIÓN 5: MENSAJE FORMATEADO ===")
# 5. Imprime un mensaje formateado con la disponibilidad
if disponible:
    disponibilidad_texto = "está disponible"
else:
    disponibilidad_texto = "no está disponible"
# Escribe aquí tu código para determinar el texto de disponibilidad

# Escribe aquí tu código para imprimir el mensaje final
print(f"El producto '{nombre}' tiene un precio de {precio}€ y actualmente {disponibilidad_texto}.")