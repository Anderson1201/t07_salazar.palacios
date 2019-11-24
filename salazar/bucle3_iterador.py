import os
# Decodificar mensaje encriptado
# S = Hola
# P = Quieres estar conmigo
# R = Te quiero

msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]


for letra in msg1:
    if letra == "S":
        print("Hola")
for letra in msg2:
    if letra == "P":
        print("Quieres  estar conmigo")
for letra in msg3:
    if letra == "R":
        print("Te quiero")

#fin_iterador

print("Fin del bucle")
