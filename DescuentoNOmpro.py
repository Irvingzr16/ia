nom=str(input("Ingresa tu nombre "))
pro=str(input("Ingresa el nombre de tu producto "))
total=float(input("ingresa el total de tu compra: "))
if total>100:
    descuento=total*.10
    totalf=total-descuento
    print(f"Felicidades! {nom} tienes un descuento de 10%. De tu producto {pro} el total a pagar es: {totalf}")
else: print(f"El total a pagar es: {total}")