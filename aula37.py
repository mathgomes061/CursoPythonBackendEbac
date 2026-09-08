# Dada uma string que consiste em palavras e espaços,
# retorne o comprimento da última palavra da string

my_string = "fly me to  the  moon "

my_list = my_string.split()

print(len(my_list[-1]))
