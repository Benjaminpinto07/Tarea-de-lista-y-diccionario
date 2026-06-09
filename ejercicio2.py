import os

inventario = {
    "Laptop": 10,
    "Mouse": 25,
    "Teclado": 15
}

os.system("cls")
print(f"Los productos que hay son {inventario}")
producto = input("Ingrese el producto que quiere solicitar: ").title()
cantidad = int(input("Ingrese la cantidad del producto: "))
if producto in inventario:
    if cantidad <= inventario[producto]:
        inventario[producto] -= cantidad
        print("Venta realizada\n")
        print(f"Stock restante de {producto}: {inventario[producto]} unidades")
    else:
        print(f"Stock insuficiente. Solo hay {inventario[producto]} unidades de {producto}")
else:
    print(f"Producto '{producto}' no encontrado en el inventario")

