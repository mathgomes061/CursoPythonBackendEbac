endereco_ip = input()

novo_endereco_ip = ""

for i in endereco_ip:
    if i == '.':
        novo_endereco_ip += "[.]"
    else:
        novo_endereco_ip += i

print(novo_endereco_ip)
