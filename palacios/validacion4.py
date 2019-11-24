import os
#Validar el codigo  de una caja fuerte
#Declarar variables
codigo=0
codigo=int(os.sys.argv[1])

codigo_invalida=(codigo < 0 or codigo > 6)

# Validar el codigo pin de un computadora del 1 al 5
while (codigo_invalida == True):
    codigo=int(os.sys.argv[1])
    codigo_invalida = (codigo < 5431 or codigo > 8123)

#fin_while
print("Fin del bucle")
