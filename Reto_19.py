print("=== PROGRAMA: SISTEMA DE PERSONAJES CON HERENCIA MÚLTIPLE ===\n")

# Clase base Personaje
class Personaje:
    def __init__(self, nombre, nivel, experiencia, vida):
        # Inicializar atributos básicos
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
        self.vida = vida
    
    def mostrar_info(self):
        # Devolver información básica del personaje
        return f"Nombre: {self.nombre} | Nivel: {self.nivel} | Experiencia: {self.experiencia} | Vida: {self.vida}"
    
    def subir_nivel(self):
        # Aumentar nivel y experiencia
        self.nivel += 1
        self.experiencia += 100
        print(f"{self.nombre} ha subido al nivel {self.nivel} (Experiencia: {self.experiencia}).")


# Clase Guerrero que hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, nivel, experiencia, vida, resistencia):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, nivel, experiencia, vida)
        # Inicializar atributo específico de Guerrero
        self.resistencia = resistencia
    
    def ataque_fisico(self):
        # Realizar ataque físico
        print(f"{self.nombre} realiza un poderoso ataque físico con resistencia {self.resistencia}.")


# Clase Mago que hereda de Personaje
class Mago(Personaje):
    def __init__(self, nombre, nivel, experiencia, vida, mana):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, nivel, experiencia, vida)
        # Inicializar atributo específico de Mago
        self.mana = mana
    
    def lanzar_hechizo(self):
        # Lanzar hechizo mágico
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.nombre} lanza un hechizo mágico. Mana restante: {self.mana}.")
        else:
            print(f"{self.nombre} no tiene suficiente mana para lanzar un hechizo.")


# Clase Paladin que hereda de Guerrero y Mago (HERENCIA MÚLTIPLE)
class Paladin(Guerrero, Mago):
    def __init__(self, nombre, nivel, experiencia, vida, resistencia, mana):
        # Llamar a los constructores de las clases padre
        Guerrero.__init__(self, nombre, nivel, experiencia, vida, resistencia)
        Mago.__init__(self, nombre, nivel, experiencia, vida, mana)
        # Inicializar atributos específicos (si se desea agregar más)
        self.titulo = "Paladín de la Luz"
    
    def mostrar_info(self):
        # Sobreescribir para mostrar información completa del paladín
        return (f"{self.titulo} {self.nombre} | Nivel: {self.nivel} | "
                f"Experiencia: {self.experiencia} | Vida: {self.vida} | "
                f"Resistencia: {self.resistencia} | Mana: {self.mana}")


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PERSONAJES ===")

# Crear una instancia de Guerrero
guerrero = Guerrero("Thorgal", 5, 1200, 150, 80)

# Crear una instancia de Mago
mago = Mago("Eldrin", 4, 950, 100, 60)

# Crear una instancia de Paladin (herencia múltiple)
paladin = Paladin("Luminor", 6, 2000, 180, 70, 50)

print("\n=== INFORMACIÓN DE PERSONAJES ===")

# Mostrar información del guerrero
print(guerrero.mostrar_info())

# Mostrar información del mago
print(mago.mostrar_info())

# Mostrar información del paladín
print(paladin.mostrar_info())

print("\n=== DEMOSTRANDO HABILIDADES ===")

# Probar habilidades del guerrero
guerrero.ataque_fisico()
guerrero.subir_nivel()

# Probar habilidades del mago
mago.lanzar_hechizo()
mago.subir_nivel()

# Probar habilidades del paladín (debe poder usar ambas)
paladin.ataque_fisico()
paladin.lanzar_hechizo()
paladin.subir_nivel()