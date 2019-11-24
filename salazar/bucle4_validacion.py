import os
# Mostrar "Acceso denegado" mientras el mensaje sea no pasar al baño
mensaje_invalida=True

while(mensaje_invalida):
    mensaje=os.sys.argv[1]
    mensaje_invalida=(mensaje != "no-pasar-al-bano")
#fin_while

print("Fin del bucle")
