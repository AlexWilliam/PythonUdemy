i = 0

while ( i <= 100):
    numDivisoes = 0
    for j in range(1, i+1):
        if( i % j == 0):
            numDivisoes += 1
            if(numDivisoes == 2) and (i == j):
                print(i)

    i += 1