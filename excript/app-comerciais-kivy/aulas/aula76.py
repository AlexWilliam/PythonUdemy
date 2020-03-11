# Operadores IN e NOT IN
# Se o 2 esta contido na tupla
2 in (1, 2, 3, 4, 5)

# Se o 6 NAO esta contido na tupla
6 not in (1, 2, 3, 4, 5)

# Se 1 esta contido dentro do intervalo
1 in range(1, 6)


x = range(1, 6)

if 3 in x:
    print("Contido!")
else:
    print("Nao esta contido!")


