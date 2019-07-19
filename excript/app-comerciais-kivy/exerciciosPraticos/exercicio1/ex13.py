dias=int(input("Informe o número de dias:"))
hora_total=input("Digite a hora(HH:mm:ss): ")
'''
Caso queira a hora separada use este codigo
hora=int(input("Digite as horas:"))
minuto=int(input("Digite os minutos:"))
segundos=int(input("Digite os segundos:"))
'''
dias_em_segundos=dias*(24*(60**2))

hora_quebrada=hora_total.split(":")

hora=int(hora_quebrada[0])
minuto=int(hora_quebrada[1])
segundos=int(hora_quebrada[2])

totalSegundos=dias_em_segundos+(hora*(60**2))+(minuto*60)+segundos

print("Total de segundos da hora", hora_total,"é",totalSegundos)