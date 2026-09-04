# decorators (decoradores) em Python servem para modificar ou aprimorar
# o comportamento de funções, métodos ou classes
# sem alterar o código original deles

def meu_decorator(func):  # Função que recebe outra função como parâmetro

    # Função wrapper, tem o papel de embrulhar a função
    # permitindo que você execute códigos antes e/ou depois
    # de a função principal rodar
    def wrapper():
        print("Antes da execução da minha despedida!")
        func()  # Executa a função original
        print("Depois da execução da minha despedida!")
    return wrapper


# Para aplicar a função decoradora, utilizar um @funcao_decoradora
# na linha acima da função a ser decorada
@meu_decorator
def despedida():
    print("Tchau!")


despedida()
