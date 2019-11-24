import os
# Decodificar mensaje encriptado
# Q = Tengo un amiga llamada Angie
# X = Angie y Eyner son novios
# Y = se casaran en enero
msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]


for letra in msg1:
    if letra == "Q":
        print("Tengo un amiga llamada Angie")
for letra in msg2:
    if letra == "X":
        print("Angie y Eyner son novios ")
for letra in msg3:
    if letra == "Y":
        print("se casaran en enero")

#fin_iterador

print("Fin del bucle")
