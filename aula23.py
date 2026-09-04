# Receba uma lista de palavras e ordene-as em ordem alfabética

my_list: list[str] = []

for i in range(1, 6):
    words = input()
    my_list.append(words)

my_list.sort()
print(my_list)

# Esse código funciona, porém em casos que sei a quantidade de repetições
# o for é uma melhor opção de loop
# while len(my_list) < 5:
#     words = input()
#     my_list.append(words)

# my_list.sort()
# print(my_list)
