# Función para solicitar el vector al usuario
def solicitar_vector(tamano):
    vector = []
    for i in range(tamano):
        dato = float(input(f"Ingrese el dato {i + 1}: "))
        vector.append(dato)
    return vector

# Función para ordenar el vector
def ordenar_vector(vector):
    return sorted(vector)

def solicitar_vector():
    """Solicita al usuario el tamaño y los datos del vector."""
    tamaño = int(input("Ingrese el tamaño del vector: "))
    vector = []
    for i in range(tamaño):
        valor = float(input(f"Ingrese el valor {i + 1}: "))
        vector.append(valor)
    return vector

def ordenar_vector(vector):
    """Ordena el vector de menor a mayor."""
    return sorted(vector)

def calcular_promedio(vector):
    """Calcula el promedio de los valores en el vector."""
    return sum(vector) / len(vector) if vector else 0

def main():
    """Función principal del programa."""
    vector = solicitar_vector()
    print("\nVector original:", vector)
    
    vector_ordenado = ordenar_vector(vector)
    print("Vector ordenado:", vector_ordenado)

    promedio = calcular_promedio(vector)
    print("Promedio de los valores:", promedio)

# Ejecutar el programa
if __name__ == "__main__":
    main()
