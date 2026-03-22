# Ejercicio 2  — “Acceso al Campus y Menú Seguro” 
# Objetivo: Login con intentos + menú de acciones con validación estricta. 
# Requisitos 
# 1. Definir credenciales fijas en el código: 
# o usuario correcto: "alumno" 
# o clave correcta: "python123" 
# 2. Permitir máximo 3 intentos para ingresar usuario y clave. 
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar. 
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 
# 1. Ver estado de inscripción (mostrar “Inscripto”) 
# 2. Cambiar clave (pedir nueva clave y confirmación; deben 
# coincidir) 
# 3. Mostrar mensaje motivacional (1 frase) 
# 4. Salir 
# 5. Validación del menú: 
# o Debe ser número (.isdigit()) 
# o Debe estar entre 1 y 4 
# Cambio de clave 
# • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, 
# rechazar. 
# Salida esperada  
# Intento 1/3 - Usuario: alumno 
# Clave: xxx 
# Error: credenciales inválidas. 
# Intento 2/3 - Usuario: alumno 
# Clave: python123 
# Acceso concedido. 
# 1) Estado  2) Cambiar clave  3) Mensaje  4) Salir 
# Opción: a 
# Error: ingrese un número válido. 
# Opción: 5 
# Error: opción fuera de rango.

# 1. Defino las credenciales fijas en el código:
usuario_correcto = "alumno"
clave_correcta = "python123"

# 2. Permito máximo 3 intentos para ingresar usuario y clave.
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    intentos += 1
    print(f"Intento {intentos}/{max_intentos}")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    # 3. Si falla 3 veces: muestro “Cuenta bloqueada” y termino.
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")
else:
    print("Cuenta bloqueada.")
    exit()

# 4. Si ingresa bien: muestro un menú repetitivo (usar while) hasta elegir salir:
while True:
    print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
    opcion = input("Opción: ")
    
    # 5. Validación del menú:
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue
    
    opcion = int(opcion)
    
    if opcion < 1 or opcion > 4:
        print("Error: opción fuera de rango.")
        continue
    
    if opcion == 1:
        print("Estado: Inscripto")
    elif opcion == 2:
        # Cambio de clave
        nueva_clave = input("Ingrese nueva clave: ")
        if len(nueva_clave) < 6:
            print("Error: la nueva clave debe tener mínimo 6 caracteres.")
        else:
            confirmacion = input("Confirme nueva clave: ")
            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                print("Clave cambiada exitosamente.")
            else:
                print("Error: las claves no coinciden.")
    elif opcion == 3:
        print("¡Nunca dejes de aprender!")
    elif opcion == 4:
        print("Hasta luego.")
        break