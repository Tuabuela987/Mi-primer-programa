mi_lista = []
intput_usuario = ""
intput_usuario = input ("¿Que necesitas comprar hoy? Escribir FIN par salir: ")

while intput_usuario != "FIN":
    intput_usuario = input("¿Que necesitas comprar hoy? Escribir FIN par salir: ")
    mi_lista.append(intput_usuario)

indice_actual = 0

while indice_actual < len(mi_lista):
    print ("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual +=1

print("Esta es la lista de la compra")