import os
#suma los x primeros números
x=int(os.sys.argv[1])
i=0
suma=0

while(i<=x):
    suma += i
    i +=1
"fin_while"
print("La suma de los ",x ,"primeros números es",suma)
