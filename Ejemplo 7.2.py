
puntos = []


lim = int(input("Escribe el limite: "))

for h in range(lim):
    print("Ingresa el valor",h+1, " : ")
    num = float(input())
    puntos.append(num)



suma = 0
for i in puntos:
    suma = i + suma
    
print ("La suma es: ",suma)

media = suma / lim
print(media)

