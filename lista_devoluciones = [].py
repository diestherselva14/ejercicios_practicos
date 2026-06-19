lista_devoluciones = []

# validar número
def pedir_monto():
    while True:
        try:
            return float(input("Monto devuelto: "))
        except ValueError:
            print("Error, ingrese un número válido.")


# registrar devolucion
def agregar():
    print("\n--- Nueva devolución ---")
    
    factura = input("Número de factura: ").strip()
    motivo = input("Motivo: ").strip()
    productos = input("Productos devueltos: ").strip()
    monto = pedir_monto()

    dato = {
        "factura": factura,
        "motivo": motivo,
        "productos": productos,
        "monto": monto
    }

    lista_devoluciones.append(dato)
    print("Guardado correctamente\n")


# mostrar todo
def ver():
    print("\n--- Lista de devoluciones ---")
    
    if not lista_devoluciones:
        print("No hay registros aún")
        return

    for i, x in enumerate(lista_devoluciones, start=1):
        print(f"""
Registro {i}
Factura: {x["factura"]}
Motivo: {x["motivo"]}
Productos: {x["productos"]}
Monto: C${x["monto"]:.2f}
        """)


# sumar montos
def total():
    suma = sum(x["monto"] for x in lista_devoluciones)
    print(f"\n Total devuelto: C${suma:.2f}")


# clasificar
def clasificar_datos():
    print("\n--- Clasificación ---")

    if not lista_devoluciones:
        print("No hay datos para clasificar")
        return

    for x in lista_devoluciones:
        if x["monto"] >= 100:
            nivel = "Alto"
        elif x["monto"] >= 50:
            nivel = "Medio"
        else:
            nivel = "Bajo"

        print(f"Factura {x['factura']} -> {nivel}")


# buscar factura (máximo 3 resultados)
def buscar_factura():
    buscar = input("Factura a buscar: ").strip()
    resultados = [x for x in lista_devoluciones if x["factura"] == buscar]

    if not resultados:
        print("No existe esa factura")
        return

    print("\n--- Resultados ---")
    for x in resultados[:3]:
        print(f"""
Factura: {x["factura"]}
Motivo: {x["motivo"]}
Productos: {x["productos"]}
Monto: C${x["monto"]:.2f}
        """)


# menú principal
def menu():
    while True:
        print("""
==== MENU ====
1. Agregar
2. Ver
3. Total
4. Clasificar
5. Buscar
6. Salir
        """)

        op = input("Opción: ").strip()

        if op == "1":
            agregar()
        elif op == "2":
            ver()
        elif op == "3":
            total()
        elif op == "4":
            clasificar_datos()
        elif op == "5":
            buscar_factura()
        elif op == "6":
            print("Adiós")
            break
        else:
            print("Opción incorrecta")


# ejecutar programa
menu()