# Retorno de valores multiplos

#def func():
#    return 1, 2

#x, y = func()

#print(x)
#print(y)


def potencia(x):
    quadrado = x**2  # calcula quadrado de x
    cubo = x**3  # calcula cubo de x
    return quadrado, cubo


q, c = potencia(10)

print(q)
print(c)
