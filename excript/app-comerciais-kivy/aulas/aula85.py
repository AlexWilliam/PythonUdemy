# Funcoes de dicionarios
tel = {}
tel = {}
tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
}

# Elementos sem ordem
print(tel)

# Retorna numero de elementos
print(len(tel))

# Remove item do dicionario
del(tel[36458899])

print(tel)

# Retorna uma lista com as chaves do dicionario
print(tel.keys())

# Retorna uma lista com os valores do dicionario
print(tel.values())

# Retorna o valor relacionado a chave informada
print(tel.get(3030122))

print("")
# Retorna um elemento e remove ele do dicionario
tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
}

print(tel)
print(tel.popitem())
print(tel)
print(tel.popitem())
print(tel)
print(tel.popitem())
print(tel)
print(tel.popitem())
print(tel)

print("")
# Retorna se o elemento esta contido ou nao no dicionario
tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
}

print(30301122 in tel)
print("")
print(30311122 in tel)

print("")
# mesclar dicionarios
tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
}

tel2 = {
    99999999: "teste1",
    55551111: "teste2"
}

tel.update(tel2)

print(tel)

print("")
# Relaciona o valor a uma tupla
tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
}

t = (10, 10, 10)
tel[t] = "eXcript"

print(tel)