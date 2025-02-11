total=float(input("ingresa el total de tu compra: "))
if total>100:
    descuento=total*.10
    totalf=total-descuento
    print(f"Felicidades! tienes un descuento de 10%. el total a pagar es: {totalf}")
else: print(f"El total a pagar es: {total}")