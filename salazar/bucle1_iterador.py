import os
# Decodificar mensaje encriptado
# A = Hola
# B = Como estas
# C = Que es de tu vida
# D = Adios
msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]
msg4=os.sys.argv[4]

for letra in msg1:
    if letra == "A":
        print("Hola")
for letra in msg2:
    if letra == "B":
        print("Como estas")
for letra in msg3:
    if letra == "C":
        print("Te estoy esperando")
for letra in msg4:
    if letra == "D":
        print("Adios")
#fin_iterador

print("Fin del bucle")
