# Definimos o uso de letras maiúsculas em uma palavra
# como correto quando o seguinte caso é válido:
# Todas as letras desta palavra são maiúsculas, como "EUA"
# Dada uma palabvra de string, retorne verdadeiro
# se o uso de letras maiúsculas está correto

my_string = "EUa"

counter = 0

for letter in my_string:
    if letter.isupper():
        counter += 1

if counter == len(my_string):
    print("Todas as letras da palvra são maiúsculas")
else:
    print("Nem todas as letras da palvra são maiúsculas")
