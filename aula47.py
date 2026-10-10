# Encontrar números repetidos na lista
# Exibir números repetidos em outra lista

my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
my_dict = {}
new_list = []

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, value in my_dict.items():
    if value > 1:
        new_list.append(key)

print(new_list)
