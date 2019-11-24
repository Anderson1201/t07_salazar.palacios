import os
# Decodificar mensaje encriptado
# A = ECOTERRA
# K = Pertenece a RED ES PAZ
# T = Unidos por el cambio

msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]


for letra in msg1:
    if letra == "A":
        print(" ECOTERRA")
for letra in msg2:
    if letra == "K":
        print("Pertenece a RED ES PAZ")
for letra in msg3:
    if letra == "T":
        print("Unidos por el cambio")

#fin_iterador

print("Fin del bucle")
