# Ejercicio 4  — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
# limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
# Variables iniciales (NO se piden por teclado)
# • energia = 100
# • tiempo = 12
# • cerraduras_abiertas = 0
# • alarma = False
# • codigo_parcial = ""
# Validaciones obligatorias
# • No usar try/except.
# 4
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# • Pedir nombre del agente y validar con .isalpha() en un while.
# • Validar opciones del menú y cualquier número pedido con .isdigit() en un
# while.
# • El juego debe funcionar con estructuras secuenciales, condicionales y
# repetitivas (puede usar funciones propias del lenguaje como .lower(), len(),
# formateo, etc.).
# Regla anti-spam (muy importante)
# Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al
# iniciar:
#  Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
# • se cobra el costo normal (-20 energía, -2 tiempo),
# • NO abre cerradura, y
# • se activa la alarma automáticamente (alarma = True) porque “la cerradura se
# trabó”.
# Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
# Menú de acciones (se repite mientras el juego siga)
# El juego continúa mientras:
# • energia > 0, tiempo > 0, cerraduras_abiertas < 3
# • y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú:
# 1. Forzar cerradura (costo: -20 energía, -2 tiempo)
# o Si la energía está por debajo de 40, hay “riesgo de alarma”:
# ▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
# o Si no hay alarma, abre 1 cerradura.
# o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y
# no abre.
# 2. Hackear panel (costo: -10 energía, -3 tiempo)
# o Debe usar un for de 4 pasos mostrando progreso.
# o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
# o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si
# todavía faltan.
# 5
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10
# energía extra)
# Regla de bloqueo por alarma
# • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema
# se bloquea y se pierde.
# Condiciones de fin
# • Si cerraduras_abiertas == 3 → VICTORIA
# • Si energia <= 0 o tiempo <= 0 → DERROTA
# • Si se bloquea por alarma → DERROTA (bloqueo)

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzadas_seguidas = 0

# Pedir nombre del agente
nombre = input("Ingrese nombre del agente: ")
while not nombre.isalpha():
    nombre = input("Error: Solo letras: ")

# Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n--- ALARMA CRÍTICA ---")
        print("El sistema se bloqueó por alarma.")
        print("DERROTA: No pudiste abrir la bóveda.")
        break

    # Mostrar estado
    print(
        f"\n--- ESTADO | Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 ---"
    )
    print("Alarma:", "ACTIVADA" if alarma else "OK")

    # Menú
    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    opcion = input("Elija acción: ")

    # Validar opción
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        opcion = input("Opción inválida. Elija 1, 2 o 3: ")

    # OPCIÓN 1: FORZAR CERRADURA
    if opcion == "1":
        forzadas_seguidas += 1

        # Regla anti-spam: 3 forzadas seguidas → alarma
        if forzadas_seguidas >= 3:
            print("\n¡La cerradura se trabó!")
            print("Se activó la alarma.")
            alarma = True
            energia -= 20
            tiempo -= 2
            forzadas_seguidas = 0  # reset
            continue

        # Costo normal
        energia -= 20
        tiempo -= 2

        # Riesgo de alarma (si energía < 40)
        if energia < 40:
            print("\n⚠️ Riesgo de alarma detectado.")
            alarma_riesgo = input("¿Forzar? (1=Sí, 2=No): ")
            while not alarma_riesgo.isdigit() or alarma_riesgo not in ["1", "2"]:
                alarma_riesgo = input("Opción inválida. 1 o 2: ")

            if alarma_riesgo == "1":
                print("¿Qué tan fuerte forzaste?")
                alarma_fuerza = input("1=Suave, 2=Normal, 3=Brutal: ")
                while not alarma_fuerza.isdigit() or alarma_fuerza not in [
                    "1",
                    "2",
                    "3",
                ]:
                    alarma_fuerza = input("Opción inválida. 1, 2 o 3: ")

                if alarma_fuerza == "3":
                    print("\n¡BRUTAL! Se activó la alarma.")
                    alarma = True
                    forzadas_seguidas = 0
                    continue

        # Abrir cerradura (si no se activó alarma)
        if not alarma:
            cerraduras_abiertas += 1
            print(f"\n✅ Cerradura abierta. Total: {cerraduras_abiertas}/3")
            forzadas_seguidas = 0

    # OPCIÓN 2: HACKEAR PANEL
    elif opcion == "2":
        forzadas_seguidas = 0
        energia -= 10
        tiempo -= 3

        print("\nIniciando hackeo...")
        for i in range(4):
            letra = input(f"Paso {i + 1}/4: Ingrese letra: ").upper()
            while not letra.isalpha() or len(letra) != 1:
                letra = input(f"Paso {i + 1}/4: Solo una letra: ").upper()

            codigo_parcial += letra
            print(f"Código parcial: {codigo_parcial}")

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(
                    f"\n✅ ¡Panel hackeado! Cerradura {cerraduras_abiertas}/3 abierta."
                )
                break

    # OPCIÓN 3: DESCANSAR
    elif opcion == "3":
        forzadas_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            print("\nDescansando con alarma activada...")
            energia -= 10
        else:
            print("\nDescansando...")

# FIN DEL JUEGO
print("\n" + "=" * 30)
print("FIN DEL JUEGO")
print("=" * 30)

if cerraduras_abiertas == 3:
    print("VICTORIA: ¡Abriste la bóveda!")
else:
    if energia <= 0:
        print("DERROTA: Te quedaste sin energía.")
    elif tiempo <= 0:
        print("DERROTA: Se acabó el tiempo.")
    elif alarma and tiempo <= 3:
        print("DERROTA: Alarma bloqueó el sistema.")
