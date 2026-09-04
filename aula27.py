my_list = [1, 2, 3, 3, 2, 4, 5, 5, 7, 6, 6]

my_dict = {}

result = 0

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, value in my_dict.items():
    if value == 1:
        result += key

print(result)
