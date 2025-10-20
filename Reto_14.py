print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializar atributos básicos
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        # Devolver información básica del producto
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock} unidades"
    
    def hay_stock(self):
        # Verificar si hay unidades disponibles
        return self.stock > 0


# Clase Alimento que hereda de Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        # Inicializar atributo específico de Alimento
        self.fecha_caducidad = fecha_caducidad
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir fecha de caducidad
        info_base = super().mostrar_info()
        return f"{info_base} | Fecha de caducidad: {self.fecha_caducidad}"


# Clase Electronico que hereda de Producto
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        # Inicializar atributo específico de Electronico
        self.garantia = garantia
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir información de garantía
        info_base = super().mostrar_info()
        return f"{info_base} | Garantía: {self.garantia} años"


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PRODUCTOS ===")

# Crear una instancia de Producto genérico
producto1 = Producto("Cuaderno", 3.50, 10)

# Crear una instancia de Alimento
alimento1 = Alimento("Manzana", 0.80, 50, "2025-12-01")

# Crear una instancia de Electronico
electronico1 = Electronico("Auriculares", 25.99, 5, 2)

print("\n=== INFORMACIÓN DE PRODUCTOS ===")

# Mostrar información del producto genérico
print(producto1.mostrar_info())

# Mostrar información del alimento
print(alimento1.mostrar_info())

# Mostrar información del electrónico
print(electronico1.mostrar_info())

print("\n=== VERIFICANDO STOCK ===")

# Verificar stock de cada producto
print(f"¿{producto1.nombre} tiene stock? {'Sí' if producto1.hay_stock() else 'No'}")
print(f"¿{alimento1.nombre} tiene stock? {'Sí' if alimento1.hay_stock() else 'No'}")
print(f"¿{electronico1.nombre} tiene stock? {'Sí' if electronico1.hay_stock() else 'No'}")