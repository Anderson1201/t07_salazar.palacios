import os
# Decodificar mensaje encriptado
# Q = Mi mascota se llama kay
# X = Kay tiene 1 año
# Y = a kay le gusta el pollo

msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]


for letra in msg1:
    if letra == "Q":
        print("Mi mascota se llama kay")
for letra in msg2:
    if letra == "X":
        print("Kay tiene 1 año ")
for letra in msg3:
    if letra == "Y":
        print("a kay le gusta el pollo")

#fin_iterador

print("Fin del bucle")
