ip = float(input("Digite o IP em decimal(999.999999999)"))

if ip < 128:
    print("IP Classe A!")
else:
    if ip < 192:
        print("IP Classe B!")
    else:
        if ip < 224:
            print("IP Classe C!")
        else:
            if ip < 240:
                print("IP Classe D!")
            else:
                print("IP Classe E!")