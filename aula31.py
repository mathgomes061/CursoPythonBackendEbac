my_list = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list_size = len(my_list)
my_list_sum = sum(my_list)

total_sum = my_list_size * (my_list_size + 1) // 2

print(total_sum - my_list_sum)
