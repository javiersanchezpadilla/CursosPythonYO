contador = 0

while contador < 5:
    print(contador)
    contador += 1

contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    if contador == 8:
        break
    print(contador)