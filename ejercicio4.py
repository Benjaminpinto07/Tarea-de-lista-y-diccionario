import os

numeros = []

for i in range(8):
    os.system("cls")
    numero = int(input(f"Ingrese el número {i+1} de 8: "))
    numeros.append(numero)

mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("\n" + "="*30)
print("RESULTADOS:")
print("="*30)
print(f"Lista de números: {numeros}")
print(f"Cantidad de elementos: {len(numeros)}")
print(f"Número MAYOR: {mayor}")
print(f"Número MENOR: {menor}")

