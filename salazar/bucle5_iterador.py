import os
# Decodificar mensaje encriptado
# L = Soy estudiante
# K = Soy alumno Unprg
# T = Me gusta el curso de programacion

msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]


for letra in msg1:
    if letra == "L":
        print("Soy universitario")
for letra in msg2:
    if letra == "K":
        print("Soy alumno Unprg")
for letra in msg3:
    if letra == "T":
        print("Me gusta el curso de programacion")

#fin_iterador

print("Fin del bucle")
