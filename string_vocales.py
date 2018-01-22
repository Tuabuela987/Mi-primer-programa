vocales = "aeiou"
l_vocales = []

frase = input("Dime una frase: ")
for i in frase:
    if i in vocales:
        l_vocales += [i]
print (l_vocales)