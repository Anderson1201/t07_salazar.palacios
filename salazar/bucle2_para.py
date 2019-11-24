import os
# Sumar los 100 primeros numeros impares

i=int(os.sys.argv[1])
suma=int(os.sys.argv[2])
while(i<=200):
    suma += i
    i += 2
#fin_while

print("La suma de los 100 primeros numeros impares es:", suma)
