lista = ["Alex", "William", "Heitor", "Carlos", "Joao"]

# Quantidade de elementos
num_itens = len(lista)

# Pega ultimo registro da lista
lista[num_itens-1]

# Insere na posicao especifica
lista.insert(2, 'Jose')

# Insere no ultimo elemento
lista.append('Jose')

# Retornar quantas vezes um elemento aparece na lista
lista.count('Jose')
# print(lista.count('Jose'))

# Retornar indice do elemento
lista.index('Carlos')
# print(lista.index('Carlos'))

print(lista)
