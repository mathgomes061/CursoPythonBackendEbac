# Dada uma lista de tamanho n, retorne o elemento majoritário
# O elemento majoritário é aquele que aparece mais de [n/s] vezes
# Você pode assumir que o elemento majoritário sempre existe na lista

my_list = [3, 2, 3, 2, 2, 4, 4, 4, 4]
my_dict = {}
n = len(my_list)

majoritary_element = n / 2

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, value in my_dict.items():
    if value >= majoritary_element:
        print(key)
