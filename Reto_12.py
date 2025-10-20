# Lista de palabras dada
palabras = ["python", "programación", "comprehension", "python", "lista", "conjunto", "programación"]

# 1. List comprehension para convertir todas las palabras a mayúsculas
palabras_mayusculas = [p.upper() for p in palabras]

# 2. Dict comprehension para crear un diccionario con palabras como claves y sus longitudes como valores
longitudes = {p: len(p) for p in palabras}

# 3. Set comprehension para obtener la primera letra de cada palabra (sin duplicados)
primeras_letras = {p[0] for p in palabras}

# Imprimir resultados para verificar
print("Lista de palabras en mayúsculas:")
print(palabras_mayusculas)

print("\nDiccionario de palabras y sus longitudes:")
print(longitudes)

print("\nConjunto de primeras letras:")
print(primeras_letras)