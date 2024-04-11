def primalidad(numero):
    contador = 0

    #Rango numerico:
    for i in range(1, numero + 1):
        if i == 1 or 1 == numero:
            continue

        #Verifica que la division del numero ingresadoes 0:
        if numero % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False
    

def main():
    numero = int(input("Ingrese un numero: "))

    if primalidad(numero):
        print(f"El numero {numero} SI es Primo ")
    else:
        print(f"El numero {numero} NO es Primo ")

if __name__ == '__main__':
    main()