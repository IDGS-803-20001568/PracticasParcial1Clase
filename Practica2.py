def obtener_lista_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        try:
            numero = int(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            return obtener_lista_numeros(cantidad)
    return numeros

def analizar_numeros(numeros):
    numeros_ordenados = sorted(numeros)
    
    print("\nNúmeros ordenados:", numeros_ordenados)

    pares = [num for num in numeros_ordenados if num % 2 == 0]
    impares = [num for num in numeros_ordenados if num % 2 != 0]

    print("\nNúmeros pares:", pares)
    print("Números impares:", impares)

    repetidos = {}
    for num in numeros_ordenados:
        if num in repetidos:
            repetidos[num] += 1
        else:
            repetidos[num] = 1

    print("\nNúmero de repeticiones:")
    for num, repeticiones in repetidos.items():
        print(f"{num}: {repeticiones} veces")

def main():
    try:
        cantidad_numeros = int(input("Ingrese la cantidad de números que desea leer: "))
        numeros = obtener_lista_numeros(cantidad_numeros)
        analizar_numeros(numeros)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
