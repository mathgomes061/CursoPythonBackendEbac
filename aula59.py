# Função normal (nomeada através do def)

# def soma(x, y):
#     return x + y


# print(soma(3, 5))

# Função lambda (função anônima)

# soma = lambda x, y: x + y

# print(soma(3, 5))

# Exemplo

lista_numeros = [1, 2, 3, 4, 5]

duplicados = map(lambda numeros: numeros * 2, lista_numeros)

print(list(duplicados))
