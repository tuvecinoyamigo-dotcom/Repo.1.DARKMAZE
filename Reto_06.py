print("=== PROGRAMA: CALCULADORA DE ÁREA DE CÍRCULO ===\n")

# Definir la función calcular_area_circulo
def calcular_area_circulo(radio):
    # 1. Definir el valor de pi
    # Escribe aquí tu código
    import math
    pi = math.pi
    
    # 2. Calcular el área usando la fórmula: π * radio²
    # Escribe aquí tu código
    area = pi * (radio ** 2)  
    
    # 3. Devolver el resultado
    # Escribe aquí tu código
    return area


print("=== PRUEBAS DE LA FUNCIÓN ===")

# Prueba 1: radio = 5
radio1 = 5
# Llamar a la función y guardar el resultado
# Escribe aquí tu código
area1 = calcular_area_circulo(radio1)

print(f"Radio: {radio1} -> Área: {area1}")

# Prueba 2: radio = 3
radio2 = 3
# Llamar a la función y guardar el resultado
# Escribe aquí tu código
area2 = calcular_area_circulo(radio2)

print(f"Radio: {radio2} -> Área: {area2}")

# Prueba 3: radio = 10.5
radio3 = 10.5
# Llamar a la función y guardar el resultado
# Escribe aquí tu código
area3 = calcular_area_circulo(radio3)

print(f"Radio: {radio3} -> Área: {area3}")

print("\n=== MODO INTERACTIVO ===")
# Solicitar al usuario un radio y calcular su área
# Escribe aquí tu código para pedir el radio al usuario
radio_usuario = input("Introduce el radio del círculo (número positivo): ")

# Convertir la entrada a número decimal
# Escribe aquí tu código
radio_usuario = float(radio_usuario)

# Llamar a la función con el radio del usuario
# Escribe aquí tu código
area_usuario = calcular_area_circulo(radio_usuario)

print(f"El área de un círculo con radio {radio_usuario} es: {area_usuario}")