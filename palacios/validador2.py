import os
#validar el porcentaje (0.1-0.48)
porcentaje_invalida=True
while (porcentaje_invalida==True):
  porcentaje=float(os.sys.argv[1])
  porcentaje_invalida=(porcentaje<=0.1 or porcentaje>=0.48)
#fin_while
print("FIN DEL BUCLE")
