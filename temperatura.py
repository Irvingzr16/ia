# Ejemplo simple de adquisición de conocimiento a través de la observación
# El sistema aprenderá la relación entre las horas del día y la temperatura promedio

datos_temperatura = {
    "mañana": 20,
    "manana": 20,  # Para aceptar "mañana" sin tilde
    "tarde": 25,
    "noche": 18,
    "medianoche": 15,
    "mediodia": 30
}

# El sistema hace predicciones de temperatura basándose en la observación
def predecir_temperatura(hora):
    hora = hora.lower()  # Convertimos a minúsculas para evitar errores
    if hora in datos_temperatura:
        return datos_temperatura[hora]
    else:
        return "Hora no válida"

# Pedir al usuario que ingrese la hora del día
hora = input("Introduce la hora del día (mañana, tarde, noche, medianoche, mediodía): ").strip().lower()

# Mostrar el resultado
print(f"La temperatura promedio en la {hora} es: {predecir_temperatura(hora)}°C")


