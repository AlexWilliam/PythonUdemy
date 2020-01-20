lista = [1, 2, 3, 4, 5]

print(lista)

#Adiciona elemento no fim
lista = lista + [6]

print(lista)

#Adiciona elemento no inicio
lista = [0] + lista

print(lista)

#Adiciona varios elementos
lista = lista + [7, 8, 9, 10]

print(lista)

#Adicionar elemento utilizando funcao
lista.append(11)

print(lista)

#Remover elementos da lista
del(lista[-1])

print(lista)
