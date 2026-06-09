import os

Lista = []
suma = 0

for x in range(5):
    os.system("cls")
    numero = int(input(f"ingrese el número{x+1}: "))
    Lista.append(numero)
    suma +=numero
    promedio = numero/5    
print(f"Lista: {Lista}\n")
print(f"Suma total: {suma}")
print(f"Promedio: {int(promedio)}")

