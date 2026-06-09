import os

notas = {
    "Pedro":5.5,
    "María":6.2,
    "Juan":4.8,
    "Ana":7.0
}

os.system("cls")
nombre = input("Ingrese un nombre: ").title()
if nombre in notas:
    print(f"La nota de {nombre} es {notas[nombre]}")
else:
    print("Alumno no encontrado")

