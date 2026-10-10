# Verifique se uma palavra foi espelhada corretamente
# Por exemplo: code -> edoc

# my_string = "code"
# new_string = my_string[::-1]

# print(new_string)

first_string = "code"
second_string = "edoc"

if first_string[::-1] == second_string:
    print("A palavra FOI espelhada corretamente")
else:
    print("A palavra NÃO FOI espelhada corretamente")
