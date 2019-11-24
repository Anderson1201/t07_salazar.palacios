import os
# Decodificar mensaje encriptado
# Roberto = 1000
# Juan = 2000
# Jordan=234
#juntos=3234
msg1=os.sys.argv[1]
msg2=os.sys.argv[2]
msg3=os.sys.argv[3]
msg4=os.sys.argv[4]


for nombre in msg1:
    if nombre == "Roberto":
        print("Tengo 1000")
for nombre in msg2:
    if nombre == "Juan":
        print("Tengo 2000 ")
for nombre in msg3:
    if nombre == "Jordan":
        print("Tengo 234")
for nombre in msg4:
    if nombre =="juntos ":
        print("juntos tienen 3234")

#fin_iterador

print("Fin del bucle")
