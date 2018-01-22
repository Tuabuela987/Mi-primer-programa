escojer_operacion = input("escoje la operacion que quieres hacer ( De Celsius a Farenheid / De Farenheid a Celsius): ")

if escojer_operacion == "De Celsius a Farenheid":
    celsius = int(input("Especifica los grados Celsius: ") )
    print ("La temperatura en Farenheid de {} grados Celsius es {}".format(celsius, celsius*1.8+32))

elif escojer_operacion == "De Farenheid a Celsius":
    farenheid = int(input("Especifica la temperatura en Farenheid: "))
    print ( "La temperatura en Celsius de {} grados Farenheid es {}".format(farenheid, (farenheid-32)/1.8))