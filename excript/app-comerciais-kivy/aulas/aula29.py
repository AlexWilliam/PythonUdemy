#print(3%2) # retorna 1

#print(4%2) # retorna 0

#print(5%2) # retorna 1

#print(7%3.1) # retorna 0.79999999999


num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

divisao = num1 / num2

resto = num1 % num2

print(num1, "dividido por", num2, "é igual a:", divisao)

print("o resto da divisao de", num1, "por", num2, "é igual a:", resto)