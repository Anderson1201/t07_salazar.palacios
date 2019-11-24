import os
# Sumar los numeros impares hasta el 800

i=int(os.sys.argv[1])
suma=int(os.sys.argv[2])
while(i<=800):
    suma += i
    i += 2
#fin_while

print("La suma de los numeros cada 3 numeros salteados es:", suma)
