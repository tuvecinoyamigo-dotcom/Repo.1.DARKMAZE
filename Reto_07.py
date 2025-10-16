def dividir_numeros():
    try:
        # Solicitar al usuario que introduzca dos números
        num1 = input("Introduce el primer número (dividendo): ")
        num2 = input("Introduce el segundo número (divisor): ")

        # Convertir las entradas a números enteros
        num1 = int(num1)
        num2 = int(num2)

        # Realizar la división del primer número entre el segundo
        resultado = num1 / num2
        print(f"El resultado de dividir {num1} entre {num2} es: {resultado}")
        return resultado

    except ValueError:
        print("Error: Debes introducir números enteros válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
    finally:
        print("Ejecución del bloque finally. Gracias por usar el programa.")

# Llamada a la función
dividir_numeros()