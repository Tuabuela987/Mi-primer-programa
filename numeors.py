numero_usuario = []
numero_del_usuario = ""

while len(numero_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
        numero_usuario.append(numero_del_usuario)
    print("Numero añadido")

