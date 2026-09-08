# Dado um número inteiro não negativo x,
# retorne a raiz quadrada de x para o número inteiro mais próximo
# O número inteiro retornado também deve ser não negativo

import math

while True:

    try:
        my_number = int(input("Digite um número inteiro e positivo: "))
    except ValueError:
        print("Digite apenas números")
        continue

    if my_number < 0:
        print("Digite um número positivo")
        continue

    result = round(math.sqrt(my_number))
    print(result)
