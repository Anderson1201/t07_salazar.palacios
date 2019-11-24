import os
#suma los x primeros números muliplos de 9
x=int(os.sys.argv[1])
i=0
suma=0

while(i<=x):
    suma += i
    i +=9
"fin_while"
print("La suma de los ",x ,"primeros números multiplos de 9 es",suma)
