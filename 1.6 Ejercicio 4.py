opciones = ["Ir al cine", "Estudiar", "Hacer ejercicio"]

def toma_decision(prioridades):
    for opcion in opciones:
        if opcion in prioridades:
            return f"El agente decide: {opcion}"
    return "El agente no decide nada"

prioridades = ["Hacer ejercicio", "Estudiar"]
print(toma_decision(prioridades))