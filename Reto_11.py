print("=== PROGRAMA: ANÁLISIS DE ESTUDIANTES POR ASIGNATURA ===\n")

# 1. Conjunto de estudiantes que cursan matemáticas (5 estudiantes)
estudiantes_matematicas = {"Ana", "Luis", "Carlos", "María", "Sofía"}

# 2. Conjunto de estudiantes que cursan física (5 estudiantes)
estudiantes_fisica = {"Luis", "María", "Pedro", "Jorge", "Sofía"}

# 3. Conjunto de estudiantes que cursan programación (5 estudiantes)
estudiantes_programacion = {"Carlos", "María", "Elena", "Sofía", "Pedro"}

print("=== CONJUNTOS INICIALES ===")
print(f"Estudiantes de Matemáticas: {estudiantes_matematicas}")
print(f"Estudiantes de Física: {estudiantes_fisica}")
print(f"Estudiantes de Programación: {estudiantes_programacion}")

print("\n=== ANÁLISIS DE INTERSECCIONES Y DIFERENCIAS ===")

# 1. Los estudiantes que cursan las tres asignaturas
tres_asignaturas = estudiantes_matematicas & estudiantes_fisica & estudiantes_programacion
print(f"Estudiantes que cursan las tres asignaturas: {tres_asignaturas}")

# 2. Los estudiantes que cursan matemáticas y física, pero no programación
mat_fis_no_prog = (estudiantes_matematicas & estudiantes_fisica) - estudiantes_programacion
print(f"Estudiantes que cursan matemáticas y física, pero no programación: {mat_fis_no_prog}")

# 3. Los estudiantes que solo cursan una asignatura
solo_matematicas = estudiantes_matematicas - (estudiantes_fisica | estudiantes_programacion)
solo_fisica = estudiantes_fisica - (estudiantes_matematicas | estudiantes_programacion)
solo_programacion = estudiantes_programacion - (estudiantes_matematicas | estudiantes_fisica)

# Unir los tres conjuntos de estudiantes que solo cursan una asignatura
solo_una_asignatura = solo_matematicas | solo_fisica | solo_programacion
print(f"Estudiantes que solo cursan una asignatura: {solo_una_asignatura}")

# 4. Todos los estudiantes únicos (el conjunto total)
todos_estudiantes = estudiantes_matematicas | estudiantes_fisica | estudiantes_programacion
print(f"Total de estudiantes únicos: {todos_estudiantes}")
print(f"Número total de estudiantes: {len(todos_estudiantes)}")