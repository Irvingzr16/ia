#Solicitamos tamaño e inicializamos
tamaño = int(input("Ingrese el tamaño del vector: "))


vector = []
for i in range(tamaño):
    dato = int(input(f"Ingrese el dato {i+1}: "))
    vector.append(dato)




# orginal
print("Vector original:", vector)





# ordenado
vector_ordenado = vector[:]
for i in range(len(vector_ordenado)):
    for j in range(i + 1, len(vector_ordenado)):
        if vector_ordenado[i] > vector_ordenado[j]:
            vector_ordenado[i], vector_ordenado[j] = vector_ordenado[j], vector_ordenado[i]





print("Vector ordenado:", vector_ordenado)


# promedio
suma = 0
for valor in vector:
    suma += valor
promedio = suma / len(vector)



print(f"El promedio de los valores es: {promedio}")