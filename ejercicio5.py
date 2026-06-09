import os

estudiantes = []

while True:
    os.system("cls")
    print("SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")
    
    opcion = input("\nSeleccione una opción (1-5): ")
    
    if opcion == "1":
        os.system("cls")
        print("AGREGAR ESTUDIANTE\n")
        nombre = input("Ingrese el nombre del estudiante: ").title()
        estudiantes.append(nombre)
        print(f"\nEstudiante '{nombre}' agregado correctamente")
        input("\nPresione Enter para continuar...")
    elif opcion == "2":
        os.system("cls")
        print("BUSCAR ESTUDIANTE\n")
        nombre = input("Ingrese el nombre a buscar: ").title()
        
        if nombre in estudiantes:
            print(f"\n Estudiante '{nombre}' ENCONTRADO")
            print(f"Posición en la lista: {estudiantes.index(nombre) + 1}")
        else:
            print(f"\nEstudiante '{nombre}' NO encontrado")
        input("\nPresione Enter para continuar...")
    elif opcion == "3":
        os.system("cls")
        print("ELIMINAR ESTUDIANTE\n")
        
        if len(estudiantes) == 0:
            print("No hay estudiantes para eliminar")
        else:
            nombre = input("Ingrese el nombre del estudiante a eliminar: ").title()
            
            if nombre in estudiantes:
                estudiantes.remove(nombre)
                print(f"\nEstudiante '{nombre}' ELIMINADO correctamente")
            else:
                print(f"\nEstudiante '{nombre}' NO encontrado")
        input("\nPresione Enter para continuar...")
    elif opcion == "4":
        os.system("cls")
        print("LISTA DE ESTUDIANTES\n")
        
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados")
        else:
            print(f"Total de estudiantes: {len(estudiantes)}\n")
            print("Lista completa:")
            print("-" * 30)
            for i, estudiante in enumerate(estudiantes, 1):
                print(f"{i}. {estudiante}")
            print("-" * 30)
        input("\nPresione Enter para continuar...")
    elif opcion == "5":
        os.system("cls")
        print("="*40)
        print("   ¡GRACIAS POR USAR EL SISTEMA!")
        print("="*40)
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione 1-5")
        input("\nPresione Enter para continuar...")