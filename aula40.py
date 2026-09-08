# Dada uma lista, retorne verdadeiro se algum valor aparecer
# pelo menos duas vezes na lista
# Retorne falso se cada elemnto for distinto

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_dict = {}

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

if any(value >= 2 for value in my_dict.values()):
    print("A lista contém elementos duplicados")
else:
    print("A lista contém apenas elementos distintos")
