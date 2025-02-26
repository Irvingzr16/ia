
# Diccionario de ciudades con temperaturas exactas
ciudades_temperatura = {
    "Ciudad de México": 22,
    "Monterrey": 30,
    "Guadalajara": 25,
    "Cancún": 28,
    "Tijuana": 18,
    "Chihuahua": 15
}

# Pedir al usuario una temperatura
temperatura_usuario = float(input("Ingresa una temperatura en °C: "))

# Buscar si la temperatura ingresada coincide con alguna ciudad
ciudad_encontrada = None  # Variable para almacenar la ciudad encontrada

for ciudad, temperatura in ciudades_temperatura.items():
    if temperatura_usuario == temperatura:
        ciudad_encontrada = ciudad
        break  # Terminamos el bucle porque ya encontramos la ciudad

# Mostrar el resultado
if ciudad_encontrada:
    print(f"La temperatura de {temperatura_usuario}°C corresponde a {ciudad_encontrada}.")
else:
    print("No existe una ciudad con esa temperatura en la lista.")
