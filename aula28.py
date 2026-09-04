my_list = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

my_dict = {}

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, value in my_dict.items():
    if value == 1:
        print(key)
