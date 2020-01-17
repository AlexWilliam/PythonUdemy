a = int(input("Digite o numero inicial do intervalo: "))
b = int(input("Digite o numero final do intervalo: "))

x = int(input("Digite um numero para excluir do print: "))
y = int(input("Digite um numero para excluir do print: "))
z = int(input("Digite um numero para excluir do print: "))

while (a <= b):
    if(a == x) or (a == y) or (a == z):
        a += 1
        continue

    print(a)
    a += 1