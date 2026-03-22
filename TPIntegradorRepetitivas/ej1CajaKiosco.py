# Ejercicio 1— “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total.
# Requisitos
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con
# .isdigit() en while).
# 3. Por cada producto (usar for):
# o Pedir precio (entero, validar .isdigit()).
# o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
# cualquier mayuscula/minuscula).
# o Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostrar:
# o Total sin descuentos
# o Total con descuentos
# o Ahorro total
# o Promedio por producto (usar float y formatear con :.2f, ejem:
# x = 3.14159
# print(f"{x:.2f}"))
# Validaciones obligatorias
# • Sin try/except.
# • No aceptar vacío en nombre (si queda vacío, es error).
# • Cantidad > 0 (si ingresa 0, volver a pedir).
# Salida esperada (ejemplo)
# Cliente: Ana
# Cantidad de productos: 3
# Producto 1 - Precio: 100  Descuento (S/N): s
# Producto 2 - Precio: 50   Descuento (S/N): n
# Producto 3 - Precio: 200  Descuento (S/N): s
# Total sin descuentos: $350
# Total con descuentos: $320.00
# Ahorro: $30.00
# Promedio por producto: $106.67
# 1

# 1. Pido nombre del cliente (solo letras, valido con .isalpha() en while).
nombre = input("Ingrese el nombre del cliente: ")
while not nombre.isalpha():
    nombre = input("Error: El nombre debe contener solo letras. Intente nuevamente: ")

# 2. Pido cantidad de productos a comprar (número entero positivo, valido con .isdigit() en while).
cantidad_str = input("Ingrese la cantidad de productos a comprar: ")
while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    cantidad_str = input(
        "Error: La cantidad debe ser un número entero positivo. Intente nuevamente: "
    )
cantidad = int(cantidad_str)

# Inicializo las variables
total_sin_descuento = 0
total_con_descuento = 0
ahorro_total = 0

# 3. Por cada producto (uso for):
for i in range(cantidad):
    # Pedir precio (entero, validar .isdigit()).
    precio_str = input(f"Ingrese el precio del producto {i + 1}: ")
    while not precio_str.isdigit():
        precio_str = input(
            f"Error: El precio debe ser un número entero. Intente nuevamente: "
        )
    precio = int(precio_str)

    # Pido si tiene descuento S/N (valido con while, acepto s o n en cualquier mayuscula/minuscula).
    tiene_descuento = input(f"¿El producto {i + 1} tiene descuento? (s/n): ").lower()
    while tiene_descuento not in ["s", "n"]:
        tiene_descuento = input(
            "Error: Debe ingresar 's' para sí o 'n' para no. Intente nuevamente: "
        ).lower()

    # Si tiene descuento: aplico el 10% al precio de ese producto.
    if tiene_descuento == "s":
        descuento = precio * 0.10
        precio_con_descuento = precio - descuento
        ahorro_total += descuento
    else:
        precio_con_descuento = precio

    # Acumulo totales
    total_sin_descuento += precio
    total_con_descuento += precio_con_descuento

# 4. Al final muestro:
print("\n" + "=" * 30)
print(f"Resumen de la compra para: {nombre}")
print("=" * 30)
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento}")
print(f"Ahorro total: ${ahorro_total}")

# Promedio por producto (uso float y formateo con :.2f)
promedio = total_con_descuento / cantidad
print(f"Promedio por producto: ${promedio:.2f}")
print("=" * 30)
