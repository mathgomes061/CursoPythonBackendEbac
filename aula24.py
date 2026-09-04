# Receba um número e determine se ele é um palíndromo
# (lê-se igual de frentre para trás)

number = int(input())

str_number = str(number)

new_number = str_number[::-1]

if new_number == str_number:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
