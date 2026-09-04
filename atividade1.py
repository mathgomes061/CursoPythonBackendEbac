produtos = {}


def adicionar_produto(produto, quantidade, preco):
    if produto not in produtos:
        produtos[produto] = {'quantidade': quantidade, 'preco': preco}
        return "Produto adicionado com sucesso."
    else:
        return "Produto já adicionado."


def listar_produtos():

    if not produtos:
        print("A lista de produtos está vazia.")
    else:
        produtos_ordenados = dict(
            sorted(produtos.items(), key=lambda item: item[0])
        )
        for produto, dados in produtos_ordenados.items():
            print(
                f"{produto}: Quantidade disponível - {dados['quantidade']} |"
                "Preço - {dados['preco']}"
                )


def remover_produto(produto):

    if produto not in produtos:
        return "Erro: produto não encontrado na lista."
    else:
        del produtos[produto]
        return "Produto removido com sucesso."


def atualizar_produto(produto, quantidade):

    if produto not in produtos:
        return "Erro: produto não encontrado na lista."
    else:
        produtos[produto]['quantidade'] = quantidade


def exibir_menu():
    return (
        "Menu: \n"
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade de produto\n"
        "5 - Sair\n"
    )


def main():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            produto = input(
                    "Digite o nome do produto a ser adicionado: "
                    )
            try:
                quantidade = int(input(
                    "Digite a quantidade do produto a ser adicionado: "
                    ))
                preco = float(input(
                    "Digite o preço do produto a ser adicionado: "
                ))
                print(adicionar_produto(produto, quantidade, preco))
            except ValueError:
                print("Digite apenas números.")

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            produto = input("Digite o nome do produto a ser removido: ")
            print(remover_produto(produto))

        elif opcao == "4":
            produto = int(input(
                "Digite o nome do produto a ser atualizado: "
                ))
            quantidade = input(
                "Digite a nova quantidade do produto a ser atualizado: "
            )
            print(atualizar_produto(produto, quantidade))

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
