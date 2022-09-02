#Lectura de 20 valores con for

lista2 =[]
for k in range(20):
    print("Ingresa el valor",k+1, " : ")
    num = int(input())
    lista2.append(num)
    
print(lista2)

for a in range(10):

    print (a)


#Escritura de veinte valores enteros

lista = []
for x in range(21):
    lista.append(x)

print(lista)

for i in lista:
    print(i)


#Lo mismo pero con while
j = 0
while j <= 20: 
    print(lista[j-1])
    j += 1




