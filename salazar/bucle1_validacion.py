import os
#Validar la edad de la Adultez
#Declarar variables
edad=0
edad=int(os.sys.argv[1])

edad_invalida=(edad < 18 or edad > 40)

# Validar que la edad promedio de la dultez esta entre 18 a 40
while (edad_invalida == True):
    edad=int(os.sys.argv[1])
    edad_invalida = (edad < 18 or edad > 40)

#fin_while
print("Fin del bucle")
