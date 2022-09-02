#Se desea contar el número de letras “a” y el número de letras “b” de una frase terminada en un punto. Se supone 
#que es posible leer los caracteres independientemente

frase = input("Dime una frase\n")
print("Número de a ", frase.count("a")+frase.count("A"))
print("Número de a ", frase.count("b")+frase.count("B"))