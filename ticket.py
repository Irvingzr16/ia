import datetime

import random

folio=random.randint(1,100)
print(f"_____________________________________________________________________")

nomt=str(input("Ingresa el nombre de la tienda: "))

nombre=input("Ingresa tu nombre ")
pro=str(input("Ingresa el nombre de tu producto "))

fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

total=float(input("ingresa el total de tu compra: "))
if total>100:
    descuento=total*.10
else: descuento=0

totalf=total-descuento
print(f"")
print(f"============================TICKET DE COMPRA=========================")
print(f"Tienda: {nomt}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha}")
print(f"--------------------------------------------------------------------")
print(f"Cliente: {nombre}")
print(f"Producto: {pro}")
print(f"Total de compra: ${total}")
print(f"Descuento aplicado: {descuento}")
print(f"Total a pagar: {totalf}")
print(f"")
print(f"---------------------------------------------------------------------")
print(f"              Gracias por su compra vuelva pronto")
print(f"=====================================================================")





