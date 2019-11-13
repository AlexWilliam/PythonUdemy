mes = int(input("Digite o numero do mes: "))

list_meses = {1 : "Janeiro", 2 : "Fevereiro", 3 : "Marco", 4 : "Abril", 5 : "Maio", 6 : "Junho", 7 : "Julho", 8 : "Agosto", 9 : "Setembro", 10 : "Outubro", 11 : "Novembro", 12 : "Dezembro"}


if mes not in list_meses:
    print("Mes invalido!")
else:
    print(list_meses[mes])