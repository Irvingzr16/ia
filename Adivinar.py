import random

num=random.randint(1,10)
adivina = int(input("Adinina el numero entre 1 y 10: "))

print(f"El numero es {num}")
if adivina==num: print("Correco! Has adivinado el numero")
else: print(f"Incorrecto! el numero era {num}")
