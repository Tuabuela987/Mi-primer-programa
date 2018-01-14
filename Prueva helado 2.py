apetece_helado = input("Te apetece un helado  (Si/No): ").upper()


if apetece_helado == "SI":
    cuanto_dinero_tienes = int(input("¿Cuanto dinero tienes?: "))
    if cuanto_dinero_tienes < 2:
        print ("no puedes comprarte un helado, trabaja para ganartelo que solo te falta {} euros" .format(2 - cuanto_dinero_tienes ))
    else:
        helados_a_comprar = cuanto_dinero_tienes//2
        if helados_a_comprar // 2 == 0:
            print ("Puedes comprarte {} helados ¡Que suerte!" .format(helados_a_comprar))
        else:
            print ("puedes comprarte {} helados¿!Que suerte!! y encima te va a sobrar {} euro/s" .format(helados_a_comprar, helados_a_comprar // 2 ))


else:
    print ("No compres helado entonces")