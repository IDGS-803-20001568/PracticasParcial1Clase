def imprimiPiramide(n):
    for i in range(1, n + 1):
      #espacios = " " * (n - i)
        asteriscos = "* " * i
        #print( espacios + asteriscos)
        print( asteriscos)

def main():
    try:
        n = int(input("Ingrese un número para la altura de la pirámide: "))
        imprimiPiramide(n)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
