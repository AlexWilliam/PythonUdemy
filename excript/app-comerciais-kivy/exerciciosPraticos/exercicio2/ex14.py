num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

valores = [num1, num2, num3]

valores.sort(reverse=True)

for i in valores:
    print(i)
