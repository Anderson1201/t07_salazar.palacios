import os
# Mostrar "Acceso denegado" mientras la clave ingresada de facebook no sea todoesposible
clave=""
clave_invalida=True

while(clave_invalida):
    clave=os.sys.argv[1]
    clave_invalida=(clave != "todosepuede")
#fin_while

print("Fin del bucle")
