# Com base em uma lista de inteiros e um limite definido
# Retorne uma lista contendo os índices dos inteiros
# em que os inteiros imediatamente anteriores a ele
# forem MAIORES que o limite
# O valor não pode ser zero

my_list = [1, 2, 3, 4, 5]
limit = 2
new_list = []

for i, value in enumerate(my_list):
    if my_list[i] - 1 > limit:
        new_list.append(i)

print(new_list)
