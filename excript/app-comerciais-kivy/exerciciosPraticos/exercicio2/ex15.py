var = input("Digite uma letra: ")

is_vogal = False

vogais = ["a", "e", "i", "o", "u"]

for letra in vogais:
    if(letra == var):
        is_vogal = True


if (is_vogal):
    print("A letra e vogal!")
else:
    print("A letra nao e vogal!")