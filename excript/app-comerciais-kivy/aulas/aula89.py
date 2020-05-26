# Parametros posicionais
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}".format(nome, sobrenome, idade, sexo))

# Parametros Posicionais
dados_pessoais("Alex", "Goncalves", 29, True)

# Parametros nomeados
dados_pessoais(idade=29, sobrenome="Goncalves", nome="Alex", sexo=True)