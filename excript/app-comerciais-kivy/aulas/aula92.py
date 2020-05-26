# Funcao Variadica
# Funcao que pode receber n parametros, sendo n >= 0

#def func(*args, ***kwargs)
#   pass


# para lista, use *args = arguments
def lista_argumentos(*lista):
    print(lista)


# para dicionarios, use **kwargs = keywords arguments
def lista_de_argumentos_assossiativos(**dicionario):
    print(dicionario)


def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)


#lista_argumentos(1, 2, 3, 4, 5, 6)
#lista_argumentos("um", "dois", "tres", "quatro")
#lista_de_argumentos_assossiativos(a=1, b=2, c=3, d=4)
#lista_de_argumentos_assossiativos(um=1, dois=2, tres=3, quatro=4)
argumentos(1, 2, 3, 4, um=1, dois=2, tres=3, quatro=4)