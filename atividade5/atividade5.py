menu_info = [
    "1 - Adicionar livro",
    "2 - Listar livros",
    "3 - Remover livro",
    "4 - Atualizar quantidade de livros",
    "5 - Registrar empréstimo",
    "6 - Exibir histórico de empréstimos",
    "7 - Sair"
]

livros_biblioteca = {}
historico_emprestimos = []


def adicionar_livro(titulo, autor, quantidade):
    if titulo not in livros_biblioteca:
        livros_biblioteca[titulo] = {'autor': autor, 'quantidade': quantidade}
        return "Livro adicionado com sucesso."

    return "Livro já adicionado."


def listar_livros():
    if not livros_biblioteca:
        return "A lista de livros está vazia."

    livros_ordenados = dict(
        sorted(livros_biblioteca.items(), key=lambda item: item[0])
    )

    livros = []

    for titulo, dados in livros_ordenados.items():
        livros.append(
            f"{titulo}: Autor - {dados['autor']} | "
            f"Quantidade disponível - {dados['quantidade']}"
        )

    return "\n".join(livros)


def remover_livro(titulo):
    if titulo not in livros_biblioteca:
        return "Erro: livro não encontrado na lista."

    del livros_biblioteca[titulo]
    return "Livro removido com sucesso."


def atualizar_livro(titulo, quantidade):
    if titulo not in livros_biblioteca:
        return "Erro: livro não encontrado na lista."

    livros_biblioteca[titulo]['quantidade'] = quantidade
    return "Livro atualizado com sucesso."


def registrar_empréstimo(titulo, quantidade):
    if titulo not in livros_biblioteca:
        return "Erro: livro não encontrado na lista."

    if quantidade <= 0:
        return "A quantidade para empréstimo deve ser maior que zero."

    if quantidade > livros_biblioteca[titulo]['quantidade']:
        return (
            "Não há quantidade desejada suficiente "
            "desse livro para empréstimo."
        )

    nova_quantidade = livros_biblioteca[titulo]['quantidade'] - quantidade
    atualizar_livro(titulo, nova_quantidade)

    historico_emprestimos.append(f"{titulo} - {quantidade}")

    return "Empréstimo registrado com sucesso."


def exibir_historico():
    if not historico_emprestimos:
        return "Histórico de empréstimos está vazio."

    return "\n".join(historico_emprestimos)


def main():
    while True:
        for item in menu_info:
            print(item)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input(
                        "Digite o título do livro a ser adicionado: "
                        )
            autor = input(
                "Digite o nome do autor do livro a ser adicionado: "
            )
            try:
                quantidade = int(input(
                    "Digite a quantidade de livros a serem adicionados: "
                    ))
                if quantidade <= 0:
                    print("A quantidade não pode ser maior do que zero.")
                    continue
            except ValueError:
                print("Digite apenas números.")
                continue

            print(adicionar_livro(titulo, autor, quantidade))

        elif opcao == "2":
            print(listar_livros())

        elif opcao == "3":
            titulo = input("Digite o título do livro a ser removido: ")
            print(remover_livro(titulo))

        elif opcao == "4":
            titulo = input("Digite o título do livro a ser atualizado: ")

            try:
                quantidade = int(input(
                    "Digite a quantidade de livros a ser atualizada: "
                    ))
                if quantidade < 0:
                    print("A quantidade não pode ser negativa.")
                    continue
            except ValueError:
                print("Digite apenas números.")
                continue

            print(atualizar_livro(titulo, quantidade))

        elif opcao == "5":
            titulo = input("Digite o título do livro a ser emprestado: ")

            try:
                quantidade = int(input(
                    "Digite a quantidade de livros a ser emprestado: "
                    ))
            except ValueError:
                print("Digite apenas números.")
                continue

            print(registrar_empréstimo(titulo, quantidade))

        elif opcao == "6":
            print("Histórico de empréstimo de livros:")
            print(exibir_historico())

        elif opcao == "7":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
