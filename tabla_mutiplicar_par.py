numero_multiplicar = int(input("Que numero vamos a multiplicar: "))
numero_tabla = int (input("Hasta que numero vamos a multiplicar: "))

for multiplo in range (numero_tabla+1):
    if (numero_multiplicar*multiplo) % 2 == 0:
        print("{}*{} = {}".format(numero_multiplicar, multiplo, numero_multiplicar * multiplo))

