import os
#suma los x primeros números multiplos de 5
x=int(os.sys.argv[1])
i=0
suma=0

while(i<=x):
    suma += i
    i +=5
"fin_while"
print("La suma de los ",x ,"multiplos de 5",suma)
