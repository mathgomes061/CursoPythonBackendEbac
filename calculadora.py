valid_operations = ["1", "2", "3", "4"]

while True:
    print("Escolha a operação a ser realizada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operation = input("Digite o número da operação desejada: ")

    if operation not in valid_operations:
        print("Erro: operação inválida. Selecione uma das opções acima.")
        continue

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Digite apenas números")

    if operation == "1":
        print("Resultado: ", num1 + num2)

    elif operation == "2":
        print("Resultado: ", num1 - num2)

    elif operation == "3":
        print("Resultado: ", num1 * num2)

    elif operation == "4":
        try:
            print("Resultado: ", num1 / num2)
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero")

    exit_calculator = False

    while True:
        print("Deseja continuar na calculadora?")
        print("1 - Continuar")
        print("2 - Sair")

        options = input("Digite o número da opção desejada: ")

        if options == "1":
            break
        elif options == "2":
            print("Saindo da calculadora.")
            exit_calculator = True
            break
        else:
            print('Selecione uma das opções acima')

    if exit_calculator:
        break
