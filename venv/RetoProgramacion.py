articulos = [
    {"código": "JO-001", "nombre": "Chocolate Amargo", "tipo": "dulce", "valor": 500 },
    {"código": "JO-002", "nombre": "Gomitas", "tipo": "dulce", "valor": 300 },
    {"código": "JO-003", "nombre": "Caramelo", "tipo": "dulce", "valor": 200 },
    {"código": "JO-004", "nombre": "Chicle Menta", "tipo": "dulce", "valor": 100 },
    {"código": "JO-005", "nombre": "Agua Mineral", "tipo": "bebida", "valor": 1600 },
    {"código": "JO-006", "nombre": "Papas Fritas", "tipo": "snack", "valor": 1200 },
    {"código": "JO-007", "nombre": "Gaseosa", "tipo": "bebida", "valor": 2500 },
    {"código": "JO-008", "nombre": "Maní Salado", "tipo": "snack", "valor": 500}
]

def ingresar_compras():
    lista_compras = []
    respuesta = "Si"
    while respuesta == "Si":
        nombre = input("Ingrese el nombre del comprador: ")
        fecha = input("Ingrese la fecha de la compra (Año-Mes-Dia): ")
        compras = []
        compra = "Si"
        while compra == "Si":
            codigo = input("Ingrese el código del producto: ")
            cantidad = int(input("Ingrese la cantidad comprada del producto: "))
            compras.append({"Codigo": codigo, "Cantidad": cantidad})
            compra = input("¿Quiere ingresar otro producto? (Si/No): ")
        lista_compras.append({"nombre": nombre, "fecha": fecha, "compras": compras})
        respuesta = input("¿Quiere ingresar otra compra? (Si/No): ")
    return lista_compras

lista_compras = ingresar_compras()

lista_compras_ordenada = sorted(lista_compras, key=lambda x: x["fecha"])

for compra_cliente in lista_compras_ordenada:
    print(f"Comprador: {compra_cliente['nombre']}")
    print(f"Fecha: {compra_cliente['fecha']}")
    for compra in compra_cliente['compras']:
        print(f"  Código: {compra['Codigo']}, Cantidad: {compra['Cantidad']}")