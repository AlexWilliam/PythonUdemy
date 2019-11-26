data = input("Digite uma data: (31/12/9999) ")

dataDividida = data.split("/")

if int(dataDividida[0]) > 31 or int(dataDividida[0]) < 0:
    print("Data invalida!")
else:
    if int(dataDividida[1]) > 12 or int(dataDividida[1]) < 0:
        print("Data invalida!")
    else:
        if int(dataDividida[2]) > 9999 or int(dataDividida[2]) < 0 or len(dataDividida[2]) < 2:
            print("Data invalida!")

