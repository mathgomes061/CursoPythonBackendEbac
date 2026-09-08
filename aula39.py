# Retorne a média de todos os salários, com exceção do maior e do menor

salary_list = [4000, 3000, 1000, 2000]

new_list = sorted(salary_list)

new_list.remove(new_list[0])
new_list.remove(new_list[-1])

salary_sum = 0

for salary in new_list:
    salary_sum += salary

result = salary_sum / len(new_list)
print(result)

# Maneira possível de resolver sem remover itens da lista
# salary_sum = 0

# for i in new_list[1:-1]:
#     print(i)
#     salary_sum += i

# result = salary_sum / (len(new_list) - 2)
# print(result)
