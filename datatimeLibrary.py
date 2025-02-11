import datetime

nombre=input("Ingresa tu nombre ")

fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Nombre del clinete: {nombre}, la fecha y hora: {fecha}")