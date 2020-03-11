# a = 10
# b = 25
# c = 66
#
# x = int(input("Digite um numero: "))
#
# '''if (x == a or x == b or x == c):
#     print("Esta contido!")
# else:
#     print("NAO esta contido!")
# '''
#
# # Com operador IN
# if x in [a, b, c]:
#     print("Esta contido!")
# else:
#     print("NAO esta contido!")
#
# # Com operador NOT IN
# if x not in [a, b, c]:
#     print("NAO esta contido!")
# else:
#     print("Esta contido!")

#-------------------------------------------------------------

cores = ["azul", "amarelo", "vermelho", "branco"]

while True:
    cor = input("Digite o nome de uma cor ou entao, "
                "0 para sair do programa: ")

    if cor == "0":
        break
    elif cor in cores:
        print("Esta contida!")
    else:
        print("NAO esta contida!")
    print()
