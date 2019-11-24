import os
# Decodificar mensaje encriptado
# F = Hola
# G = Soy Anderson
# H = me gusta jugar
# I = adios
msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]
msg4=os.sys.argv[4]

for letra in msg1:
    if letra == "F":
        print("Hola")
for letra in msg2:
    if letra == "G":
        print("Soy Anderson")
for letra in msg3:
    if letra == "H":
        print("Me gusta jugar")
for letra in msg4:
    if letra == "I":
        print("Adios")
#fin_iterador

print("Fin del bucle")
