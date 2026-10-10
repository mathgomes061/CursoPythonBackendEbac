# Dada uma lista aleatória:
# Retorne o menor número inteiro e positivo
# que não está presente na lista
# Ex: [2, 3, 4] -> 1 ou [1, 4, 9] -> 2

from collections import Counter

my_list = [3, 2, 0]
my_dict = {}  # type: ignore
counter_number = 1

my_dict = Counter(my_list)

while True:
    if counter_number in my_dict:
        counter_number += 1
    else:
        print(counter_number)
        break
