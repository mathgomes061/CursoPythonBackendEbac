# Soma de 1 a N:
# Receba um número N e exiba a soma de todos os números de 1 até N

number = int(input())
result = 0

for i in range(1, number + 1):
    result += i

print(result)
