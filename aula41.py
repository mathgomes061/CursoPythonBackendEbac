# Dada uma lista, definimos uma soma acumulada de uma lista como
# runningSum[i] = sum(my_list[0] + my_list[i])
# Retorne a soma acumulada da lista
# Explicação: A soma acumulada é obtida da seguinte forma:
# [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]

my_list = [1, 2, 3, 4]
result_list = []

counter = 0

for i in my_list:
    counter += i
    result_list.append(counter)

print(result_list)
