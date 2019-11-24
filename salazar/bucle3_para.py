import os
# Sumar los numeros pares hasta el 500

i=int(os.sys.argv[1])
suma=int(os.sys.argv[2])
while(i<=500):
    suma += i
    i += 2
#fin_while

print("La suma de los numeros pares hasta el 500 es:", suma)
