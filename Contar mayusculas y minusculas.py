mayusculas = "QWERTYUIOPASDFGHJKLZXCVBNM"
n_mayusculas = 0
n_minusculas = 0
frase = input("Introduce una frase: ")

for i in frase:
    if i in mayusculas:
        n_mayusculas +=1
    else:
        n_minusculas +=1

print ("Hay {} mayusculas y {} minusculas".format(n_mayusculas, n_minusculas))