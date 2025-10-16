# Solicitar la edad al usuario
# Convertir la entrada a entero
# Evaluar la edad usando if-elif-else
# Mostrar el mensaje correspondiente

edad = int(input("Por favor, ingresa tu edad: "))
if edad < 0:
    print("Edad no válida.")    
elif edad < 13:
    print("Eres un niño.")  
elif edad < 20:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")    
else:
    print("Eres un adulto mayor.")
    
print("Fin del programa.")
