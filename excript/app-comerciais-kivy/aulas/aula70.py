#Iterando listas com python

#Iteracao com range
lista_nums = [100, 200, 300, 400]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000

print(lista_nums)

#Iterando com enumerate
lista_nums = [100, 200, 300, 400]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000

print(lista_nums)

