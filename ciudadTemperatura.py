ciudades_temperatura = {
    "Ciudad de México": 18,
    "Monterrey": 21,
    "Guadalajara": 19,
    "Cancún": 20,
    "Tijuana": 17,
    "Chihuahua": 15,
    "Tlaxiaco":16,
    "Toluca": 22,
}


temperatura_usuario = float(input("Ingresa una temperatura en °C: "))

ciudad_encontrada = None

for ciudad, temperatura in ciudades_temperatura.items():
    if temperatura_usuario == temperatura:
        ciudad_encontrada = ciudad
        break

if ciudad_encontrada:
    print(f"La temperatura de {temperatura_usuario}°C corresponde a {ciudad_encontrada}.")
else:
    print("No existe una ciudad con esa temperatura en la lista.")
