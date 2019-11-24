import os
# Sumar los 50 primeros numeros

i=int(os.sys.argv[1])
suma=int(os.sys.argv[2])
while(i<=50):
    suma += i
    i += 1
#fin_while

print("La suma de los 50 primeros numeros es:", suma)
