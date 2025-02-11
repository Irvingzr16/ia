def generar_tabla_multiplicar(numero):
    return [f"{numero} * {i:02} = {numero * i:02}" for i in range(1, 11)]

def main():
    try:
        numero = int(input("Ingresa un número: "))
        print("\n".join(generar_tabla_multiplicar(numero)))
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
