my_list = [1, 2, 3, 3, 4, 4, 5, 6, 7, 1, 2, 3]
my_dict = {}

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, value in my_dict.items():
    if key == value:
        print(f'{key} é um número inteiro sortudo')
