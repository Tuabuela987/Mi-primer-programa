pokemon_elegido = input ("¿Contra quien quieres luchar? (Squirtle / Charmander / Bulbasure): ")
vida_pikachu = 100
vida_enemigo = 0
dano_enemigo = 0


if pokemon_elegido == "Squirtle":
    vida_enemigo = 100
    dano_enemigo = 90

elif pokemon_elegido == "Charmander":
    vida_enemigo = 90
    dano_enemigo = 10
elif pokemon_elegido == "Bulbasure":
    vida_enemigo = 80
    dano_enemigo = 12

while vida_enemigo >= 0 and vida_pikachu >= 0:
    ataque_pikachu = input("¿Que ataque vamos a usar? (Chispazo / Bola Voltio): ")
    if ataque_pikachu == "Bola Voltio":
        vida_enemigo -= 12
    elif ataque_pikachu == "Chispazo":
        vida_enemigo -= 10

    vida_pikachu -= dano_enemigo

    print (("La vida de pikachu es {}") .format(vida_pikachu))
    print (("La vida de {} es {}").format (pokemon_elegido, vida_enemigo))

if vida_pikachu <= 0:
    print(("Gana {}").format(pokemon_elegido))
else:
    print("Tu ganas pikachu")
