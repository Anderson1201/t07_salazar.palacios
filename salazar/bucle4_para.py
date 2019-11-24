import os
# Sumar los numeros cada 3 numeros salteados hasta el 120

i=int(os.sys.argv[1])
suma=int(os.sys.argv[2])
while(i<=120):
    suma += i
    i += 3
#fin_while

print("La suma de los numeros cada 3 numeros salteados es:", suma)
