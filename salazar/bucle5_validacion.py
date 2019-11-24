import os
# Mostrar numero de accidentes anuales de 100 a 200
accidente_invalida=True

while(accidente_invalida):
    accidente=int(os.sys.argv[1])
    accidente_invalida=(accidente<100 or accidente>200)
#fin_while

print("Fin del bucle")
