import os
#validar la temperatura (58.5-68.5)
tem_invalida=True
while (tem_invalida==True):
    temp=float(os.sys.argv[1])
    tem_invalida=(temp<58.5 or temp>68.5)
#fin_while
print("FIN DEL BUCLE")
