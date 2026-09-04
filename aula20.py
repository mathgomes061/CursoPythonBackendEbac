# Receba um número e exiba a tabuada de 1 a 10 para ele

number = float(input())
# multiplier = 1

# while multiplier <= 10:
#     result = number * multiplier
#     print(result)

#     multiplier = multiplier + 1

for i in range(1, 11):
    result = number * i
    print(result)
