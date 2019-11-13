numero1 = int(input("Digite o primeiro numero a ser verificado: "))

numero2 = int(input("Digite o segundo numero a ser verificado: "))

if(numero1 > numero2):
    print(numero1)
    print(numero2)
else:
    if(numero2 > numero1):
        print(numero2)
        print(numero1)
    else:
        print("numeros identicos!")