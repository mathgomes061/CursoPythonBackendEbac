# Considere palavras longas como
# palavras com mais de 10 caracteres
# Todas as palavras longas devem ser substituidas
# da seguinte forma:
# - A primeira letra
# - a quantidade de caracteres entre a primeira e a última letra
# - a útima letra
# Exemplo: "localization" = l10n
# O número está no sistema decimal e não contém zeros à esquerda

my_string = "localization"


def abbreviate_string(string: str):
    if len(string) > 10:
        string = string[0] + str(len(string) - 2) + string[-1]
        print(string)
    else:
        print(string)


abbreviate_string(my_string)

# Sem utilizar uma função:
# if len(my_string) > 10:
#     print(f"{my_string[0]}{str(len(my_string) - 2)}{my_string[-1]}")
# else:
#     print(my_string)
