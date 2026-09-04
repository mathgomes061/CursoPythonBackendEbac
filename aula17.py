# Escreva um programa que receba 3 números e exiba o segundo maior entre eles.

# 1. Receber números separadamente

# Para dar valores a várias variáveis ao mesmo tempo ao utilizar o input
# utilizar a função map, juntamente com o split
number1, number2, number3 = map(int, input().split())

# 2. Criar lógica para verificar qual o segundo maior

my_list = []

my_list.append(number1)
my_list.append(number2)
my_list.append(number3)

# Ordena os itens da lista
my_list.sort()

# 3. Mostrar na tela o quem é o segundo maior

print(my_list[1])
