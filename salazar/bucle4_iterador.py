import os
# Decodificar mensaje encriptado
# w = Soy Anderson
# x = soy grupo con Pierina
# y = Se trabaja bien con ella
# z = Gracias
msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]
msg4=os.sys.argv[4]

for letra in msg1:
    if letra == "w":
        print("Soy Anderson")
for letra in msg2:
    if letra == "x":
        print("soy grupo con Pierina")
for letra in msg3:
    if letra == "y":
        print("Se trabaja bien con ella")
for letra in msg4:
    if letra == "z":
        print("Gracias")
#fin_iterador

print("Fin del bucle")
