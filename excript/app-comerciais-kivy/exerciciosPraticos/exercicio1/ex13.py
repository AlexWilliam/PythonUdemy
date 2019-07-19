hora_total=input("Digite a hora(HH:mm:ss): ")

hora_quebrada=hora_total.split(":")

hora=int(hora_quebrada[0])
minuto=int(hora_quebrada[1])
segundos=int(hora_quebrada[2])

totalSegundos=(hora*(60**2))+(minuto*60)+segundos

print("Total de segundos da hora", hora_total,"é",totalSegundos)