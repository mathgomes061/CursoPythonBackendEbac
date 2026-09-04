numbers = [12, 345, 2, 6, 7896]

new_list = []

for i in numbers:
    new_number = str(i)
    if len(new_number) % 2 == 0:
        new_list.append(i)

print(new_list)
print(f'{len(new_list)} valores da lista contêm um número par de digitos')
