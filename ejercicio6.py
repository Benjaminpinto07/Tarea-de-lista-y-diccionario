import os

estudiantes = {}

while True:
    os.system("cls")
    print("=== SISTEMA DE ESTUDIANTES ===")
    print("1. Agregar estudiante")
    print("2. Agregar nota")
    print("3. Mostrar estudiantes")
    print("4. Mostrar promedio de un estudiante")
    print("5. Mostrar todos los promedios")
    print("6. Salir")
    
    opcion = input("\nOpción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ").title()
        if nombre in estudiantes:
            print("Ya existe")
        else:
            estudiantes[nombre] = []
            print("Agregado")
        input("Enter...")
    
    elif opcion == "2":
        nombre = input("Nombre: ").title()
        if nombre not in estudiantes:
            print("No existe")
        else:
            nota = float(input("Nota: "))
            if 1.0 <= nota <= 7.0:
                estudiantes[nombre].append(nota)
                print("Nota agregada")
            else:
                print("Nota inválida")
        input("Enter...")
    
    elif opcion == "3":
        print("\nEstudiantes:")
        for nombre in estudiantes:
            print(f"• {nombre}")
        if not estudiantes:
            print("Lista vacía")
        input("\nEnter...")
    
    elif opcion == "4":
        nombre = input("Nombre: ").title()
        if nombre in estudiantes and estudiantes[nombre]:
            promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
            print(f"Promedio: {promedio:.2f}")
        else:
            print("No se puede calcular")
        input("Enter...")
    
    elif opcion == "5":
        print("\nPromedios:")
        for nombre, notas in estudiantes.items():
            if notas:
                promedio = sum(notas) / len(notas)
                print(f"{nombre}: {promedio:.2f}")
            else:
                print(f"{nombre}: Sin notas")
        input("\nEnter...")
    
    elif opcion == "6":
        print("¡Adiós!")
        break
    
    else:
        print("Opción inválida")
        input("Enter...")