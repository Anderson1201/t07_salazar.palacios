import os
# Decodificar mensaje encriptado
# A = Soy mujer
# K = me llamo Pierina
# T = Me gusta el voley

msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]


for letra in msg1:
    if letra == "A":
        print("Soy mujer")
for letra in msg2:
    if letra == "K":
        print("Me llamo Pierina")
for letra in msg3:
    if letra == "T":
        print("Me gusta el voley")

#fin_iterador

print("Fin del bucle")
