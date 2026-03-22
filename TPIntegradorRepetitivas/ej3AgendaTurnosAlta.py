#  Ejercicio 3 (Alta) — “Agenda de Turnos con
# Nombres (sin listas)”
# Contexto
# Hay 2 días de atención: Lunes y Martes.
# Cada día tiene cupos fijos:
# • Lunes: 4 turnos
# • Martes: 3 turnos
# Reglas
# 1. Pedir nombre del operador (solo letras).
# 2. Menú repetitivo hasta salir:
# 1. Reservar turno
# 2. Cancelar turno (por nombre)
# 3. Ver agenda del día
# 4. Ver resumen general
# 5. Cerrar sistema
# 3. Reservar:
# o Elegir día (1=Lunes, 2=Martes).
# o Pedir nombre del paciente (solo letras).
# o Verificar que no esté repetido en ese día (comparando con las variables
# ya cargadas).
# o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
# 4. Cancelar:
# o Elegir día.
# o Pedir nombre del paciente (solo letras).
# o Si existe, cancelar y dejar el espacio vacío ("").
# 5. Ver agenda del día:
# 3
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
# está vacío.
# 6. Resumen general:
# o Turnos ocupados y disponibles por día.
# o Día con más turnos (o empate).
# Restricciones
# •  No listas, no diccionarios, no sets, no tuplas.
# •  Se permite usar "" como “vacío”.
# •  Validaciones con .isalpha() y .isdigit() (sin try/except).


# Variables iniciales
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    operador = input("Error: Use solo letras: ")

while True:
    print(f"\n--- Sistema de Turnos | Operador: {operador} ---")
    print("1. Reservar\n2. Cancelar\n3. Ver Agenda\n4. Resumen\n5. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        dia = input("Día (1=Lunes, 2=Martes): ")
        nombre = input("Paciente: ")
        while not nombre.isalpha():
            nombre = input("Solo letras: ")

        if dia == "1":
            if (
                nombre == lunes1
                or nombre == lunes2
                or nombre == lunes3
                or nombre == lunes4
            ):
                print("Error: Ya tiene turno este día.")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("Lunes lleno.")
        elif dia == "2":
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Error: Ya tiene turno.")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("Martes lleno.")

    elif opcion == "2":
        dia = input("Día (1=Lunes, 2=Martes): ")
        nombre = input("Paciente a cancelar: ")
        if dia == "1":
            if nombre == lunes1:
                lunes1 = ""
            elif nombre == lunes2:
                lunes2 = ""
            elif nombre == lunes3:
                lunes3 = ""
            elif nombre == lunes4:
                lunes4 = ""
            else:
                print("No se encontró.")
        elif dia == "2":
            if nombre == martes1:
                martes1 = ""
            elif nombre == martes2:
                martes2 = ""
            elif nombre == martes3:
                martes3 = ""
            else:
                print("No se encontró.")

    elif opcion == "3":  # REGLA 5: Mostrar (libre)
        dia = input("Día (1=Lunes, 2=Martes): ")
        if dia == "1":
            print("Agenda Lunes:")
            print(f"1. {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"2. {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"3. {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"4. {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print("Agenda Martes:")
            print(f"1. {martes1 if martes1 != '' else '(libre)'}")
            print(f"2. {martes2 if martes2 != '' else '(libre)'}")
            print(f"3. {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == "4":  # REGLA 6: Cálculos sin listas
        # Contadores manuales
        ocu_lun = 0
        ocu_mar = 0
        if lunes1 != "":
            ocu_lun += 1
        if lunes2 != "":
            ocu_lun += 1
        if lunes3 != "":
            ocu_lun += 1
        if lunes4 != "":
            ocu_lun += 1

        if martes1 != "":
            ocu_mar += 1
        if martes2 != "":
            ocu_mar += 1
        if martes3 != "":
            ocu_mar += 1

        dis_lun = 4 - ocu_lun
        dis_mar = 3 - ocu_mar

        print("--- RESUMEN ---")
        print(f"Lunes: {ocu_lun} ocupados, {dis_lun} disponibles.")
        print(f"Martes: {ocu_mar} ocupados, {dis_mar} disponibles.")

        # Comparación de mayor ocupación
        if ocu_lun > ocu_mar:
            print("Día con más turnos: Lunes")
        elif ocu_mar > ocu_lun:
            print("Día con más turnos: Martes")
        else:
            print("Día con más turnos: Empate")

    elif opcion == "5":
        break
