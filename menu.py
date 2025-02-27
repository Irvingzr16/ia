import os

def menu():
    print("Seleccione el ejercicio que desea ejecutar:")
    print("1. 1.8.3 Algoritmo de busqueda local")
    print("2. 1NombreEdad")
    print("3. 2Promedio")
    print("4. Adivinar")
    print("5. CalificacionLetra")
    print("6. circulo")
    print("7. ciudadTemperatura")
    print("8. datatimeLibrary")
    print("9. Descuento")
    print("10. DescuentoNOmpro")
    print("11. elif")
    print("12. Examen")
    print("13. ExamenC")
    print("14. for")
    print("15. from pytube import YouTube")
    print("16. IA-PRACT-15.docx")
    print("17. ifelse_mucho")
    print("18. ifelsemateria")
    print("19. imprimir")
    print("20. nodo")
    print("21. paroImpar")
    print("22. Positivo-o-negativo")
    print("23. promedio")
    print("24. razonamiento")
    print("25. restaYmultiplicacion")
    print("26. school")
    print("27. suma de consola")
    print("28. suma=2")
    print("29. Tabla")
    print("30. temperatura")
    print("31. ticket")
    print("32. 1.6 Ejercicio 4")
    print("33. 1.7 Ejercicio - 2 Agentes")
    print("34. 1.8 El papel de la heuristica")
    print("35. 1.8.1 Algoritmos de exploracion de alternativas")
    print("36. 1.8.1 eJERCICIO")
    print("37. 1.8.2 Algoritmo A")

    choice = int(input("Ingrese el número del ejercicio: "))

    exercises = {
        1: "c:\\Users\\irvin\\Documents\\IA\\1.8.3 Algoritmo de busqueda local.py",
        2: "c:\\Users\\irvin\\Documents\\IA\\1NombreEdad.py",
        3: "c:\\Users\\irvin\\Documents\\IA\\2Promedio.py",
        4: "c:\\Users\\irvin\\Documents\\IA\\Adivinar.py",
        5: "c:\\Users\\irvin\\Documents\\IA\\CalificacionLetra.py",
        6: "c:\\Users\\irvin\\Documents\\IA\\circulo.py",
        7: "c:\\Users\\irvin\\Documents\\IA\\ciudadTemperatura.py",
        8: "c:\\Users\\irvin\\Documents\\IA\\datatimeLibrary.py",
        9: "c:\\Users\\irvin\\Documents\\IA\\Descuento.py",
        10: "c:\\Users\\irvin\\Documents\\IA\\DescuentoNOmpro.py",
        11: "c:\\Users\\irvin\\Documents\\IA\\elif.py",
        12: "c:\\Users\\irvin\\Documents\\IA\\Examen.py",
        13: "c:\\Users\\irvin\\Documents\\IA\\ExamenC.py",
        14: "c:\\Users\\irvin\\Documents\\IA\\for.py",
        15: "c:\\Users\\irvin\\Documents\\IA\\from pytube import YouTube.py",
        16: "c:\\Users\\irvin\\Documents\\IA\\IA-PRACT-15.docx",
        17: "c:\\Users\\irvin\\Documents\\IA\\ifelse_mucho.py",
        18: "c:\\Users\\irvin\\Documents\\IA\\ifelsemateria.py",
        19: "c:\\Users\\irvin\\Documents\\IA\\imprimir.py",
        20: "c:\\Users\\irvin\\Documents\\IA\\nodo.py",
        21: "c:\\Users\\irvin\\Documents\\IA\\paroImpar.py",
        22: "c:\\Users\\irvin\\Documents\\IA\\Positivo-o-negativo.py",
        23: "c:\\Users\\irvin\\Documents\\IA\\promedio.py",
        24: "c:\\Users\\irvin\\Documents\\IA\\razonamiento.py",
        25: "c:\\Users\\irvin\\Documents\\IA\\restaYmultiplicacion.py",
        26: "c:\\Users\\irvin\\Documents\\IA\\school.py",
        27: "c:\\Users\\irvin\\Documents\\IA\\suma de consola.py",
        28: "c:\\Users\\irvin\\Documents\\IA\\suma=2.py",
        29: "c:\\Users\\irvin\\Documents\\IA\\Tabla.py",
        30: "c:\\Users\\irvin\\Documents\\IA\\temperatura.py",
        31: "c:\\Users\\irvin\\Documents\\IA\\ticket.py",
        32: "c:\\Users\\irvin\\Documents\\IA\\1.6 Ejercicio 4.py",
        33: "c:\\Users\\irvin\\Documents\\IA\\1.7 Ejercicio - 2 Agentes.py",
        34: "c:\\Users\\irvin\\Documents\\IA\\1.8 El papel de la heuristica.py",
        35: "c:\\Users\\irvin\\Documents\\IA\\1.8.1 Algoritmos de exploracion de alternativas .py",
        36: "c:\\Users\\irvin\\Documents\\IA\\1.8.1 eJERCICIO .py",
        37: "c:\\Users\\irvin\\Documents\\IA\\1.8.2 Algoritmo A.py"
    }

    if choice in exercises:
        os.system(f'python "{exercises[choice]}"')
    else:
        print("Opción no válida")

if __name__ == "__main__":
    while True:
        menu()
        exit_choice = input("Ingrese '0' para salir o cualquier otra tecla para continuar")
        if exit_choice == '0':
            break