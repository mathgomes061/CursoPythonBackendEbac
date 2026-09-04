# List comprehension
# Uma maneira de rodar um loop em apenas uma linha de código
# e guardar isso dentro de uma variável
my_list = [elemento for elemento in range(1, 6)]

print(my_list)

# Exemplo

palavras = ["python", "é", "divertido"]

# Loop usando for
# for palavra in palavras:
#     print(palavra[0])

# Usando list comprehension
iniciais = [palavra[0] for palavra in palavras]
print(iniciais)


# Exemplo 2
# Mostrar o quadrado de  de 1 a 10 apenas se o quadrado for um númeor ímpar

# Loop usando for
lista_numeros = []

for numero in range(1, 11):
    lista_numeros.append(numero ** 2)

for numero in lista_numeros:
    if numero % 2 != 0:
        print(numero)


# # Usando list comprehension
quadrados_impares = [
    elemento**2 for elemento in range(1, 11) if elemento % 2 != 0
    ]
print(quadrados_impares)
