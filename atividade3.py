valid_operations = ["1", "2", "3", "4"]
menu_info = ["1 - Soma", "2 - Subtração", "3 - Multiplicação", "4 - Divisão"]


def check_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Digite apenas números")


while True:
    _ = [print(item) for item in menu_info]

    operation = input("Digite o número da operação desejada: ")

    if operation not in valid_operations:
        print("Erro: operação inválida. Selecione uma das opções acima.")
        continue

    num1 = check_number("Digite o primeiro número: ")

    if operation == "4":
        result = lambda x, y: x / y

        while True:
            num2 = check_number("Digite o segundo número: ")

            try:
                print("Resultado:", result(num1, num2))
                break
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero.")

    else:
        num2 = check_number("Digite o segundo número: ")

        if operation == "1":
            result = lambda x, y: x + y
            print("Resultado: ", result(num1, num2))

        elif operation == "2":
            result = lambda x, y: x - y
            print("Resultado: ", result(num1, num2))

        elif operation == "3":
            result = lambda x, y: x * y
            print("Resultado: ", result(num1, num2))

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
