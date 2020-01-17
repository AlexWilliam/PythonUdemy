i = int(input("Digite o numero inicial do intervalo: "))
z = int(input("Digite o numero final do intervalo: "))

while ( i <= z):
    numDivisoes = 0
    for j in range(1, i+1):
        if( i % j == 0):
            numDivisoes += 1
            if(numDivisoes == 2) and (i == j):
                print(i)

    i += 1