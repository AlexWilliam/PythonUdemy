#adicionando, removendo e editando elementos de listas
l = ['bbb', 'ccc', 'ddd']
print(l)

#adiciona ao final
l.append('eee')
print(l)

#Adiciona em uma posicao espedifica
l.insert(0, 'aaa')
print(l)

#Alterar o elemento da lista
l[1] = 'bbbb'
print(l)

#deletar elementos da lista

#limpa a lista
l.clear()
print(l)

l = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

#excluir ultimo elemento da lista
#pop retorna o elemento excluido
l.pop()
print(l)

#excluindo elemento especifico
l.pop(0)
print(l)

l = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

#deletar intervalos de indices
del(l[2:4])

l = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

#deletar alternando elementos, pulando de dois em dois
del(l[::2])
print(l)
