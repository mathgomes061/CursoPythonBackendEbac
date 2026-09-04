# O yield permite que a função fique salva na memória
# e só seja executada quando for chamada
# (por exemplo através do next)

def counter_function():
    yield 1
    yield 2
    yield 3


contador = counter_function()

print(next(contador))
print(next(contador))
print(contador)
