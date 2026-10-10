# Dada uma lista de inteiros:
# sum1 é a soma de todos os inteiros com apenas UM digito E
#  os inteiros com DOIS digitos
# sum2 é a soma dos inteiros restantes
# Retorne verdadeiro caso sum1 > sum2

numbers = [1, 2, 3, 4, 10, 100, 500, 600]
sum1 = 0
sum2 = 0

for number in numbers:
    if number >= 100:
        sum2 += number
    else:
        sum1 += number

if sum1 > sum2:
    print(True)
else:
    print(False)
