number_to_guess = 2
user_number1 = int (input("adivina el numero: "))

if not number_to_guess == user_number1:
    print ("Repite otra vez")

    user_number2 = int(input("Prueva con otro: "))
    if not number_to_guess == user_number2:
        print ("Repite otra vez")

        user_number3= int(input("Prueva con otro: "))
        if not number_to_guess == user_number3:
            print ("Repite otra vez")

            user_number4 = int(input("Prueva con otro: "))
            if not number_to_guess == user_number4:
                print ("Repite otra vez")

                user_number5 = int(input("Prueva con otro:"))
                if not number_to_guess == user_number5:
                    print ("Game Over")

else:
    print ("You Win")