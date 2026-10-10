# Dada uma lista de strings e um caractere:
# Retorne uma lista dos ídices das strings
# que contenham o caractere

my_list = ["leet", "code", "lindo"]
char = "e"
new_list = []

for i, string in enumerate(my_list):
    if char in string:
        new_list.append(i)

print(new_list)
