""" Sistema de Gerenciamento de Pokémon

Descrição: Programa para adicionar, listar, remover e atualizar nível
do Pokémon, registrar capturas e consultar o histórico de capturas.

Como executar:

Instale o Python 3, caso ainda não esteja instalado.
Salve este arquivo com o nome gerenciamento_pokemon.py.
Abra um terminal na pasta onde o arquivo foi salvo.
Execute o comando:
python gerenciamento_pokemon.py

Em alguns sistemas, pode ser necessário utilizar:
python3 gerenciamento_pokemon.py """

# Menu principal com opções para o usuário
menu_info = [
    "1 - Adicionar Pokémon",
    "2 - Listar Pokémons",
    "3 - Remover Pokémon",
    "4 - Atualizar nível de Pokémons",
    "5 - Registrar captura",
    "6 - Exibir histórico de capturas",
    "7 - Sair"
]

# Dicionário para armazenar os Pokémons, utilizando o nome como chave
# Cada Pokémon possuí um tipo, nivel e quantidade de capturas
pokemons = {}

# Lista que armazena o histórico de capturas dos Pokémons
historico_capturas = []


def adicionar_pokemon(nome, tipo, nivel):
    """Cadastra um Pokémon após validar o seu nível"""
    if type(nivel) is not int or not 1 <= nivel <= 100:
        return "Erro: o nível deve ser um inteiro entre 1 e 100."

    if nome not in pokemons:
        pokemons[nome] = {
            "tipo": tipo,
            "nivel": nivel,
            "capturas": 0
        }
        return "Pokémon adicionado com sucesso"

    return "Pokemon já cadastrado"


def listar_pokemons():
    """Exibe os Pokémons cadastrados em ordem alfabética"""
    if not pokemons:
        return "A lista está vazia."

    lista_pokemons = []

    for nome, dados in sorted(
        pokemons.items(),
        key=lambda item: item[0].casefold()
    ):
        lista_pokemons.append(
            f"{nome} - {dados['tipo']} - {dados['nivel']}"
        )

    return "\n".join(lista_pokemons)


def remover_pokemon(nome):
    """Remove um Pokémon, caso ele exista no dicionário"""
    if nome not in pokemons:
        return "Erro: não há nenhum Pokémon com esse nome."

    del pokemons[nome]
    return "Pokémon removido com sucesso"


def atualizar_nivel(nome, novo_nivel):
    """Atualiza o nível do Pokémon, após validar seus dados"""
    if nome not in pokemons:
        return "Erro: não há nenhum pokémon com esse nome."

    if type(novo_nivel) is not int or not 1 <= novo_nivel <= 100:
        return "Erro: o nível deve ser um inteiro entre 1 e 100."

    pokemons[nome]["nivel"] = novo_nivel
    return "Nivel do Pokémon atualizado com sucesso."


def registrar_captura(nome, quantidade):
    """Atualiza a contagem e registra a captura em um histórico"""
    if nome not in pokemons:
        return "Erro: não há nenhum Pokémon com esse nome."

    if type(quantidade) is not int or quantidade <= 0:
        return "Erro: a quantidade deve ser um inteiro maior que zero."

    pokemons[nome]["capturas"] += quantidade

    historico_capturas.append((nome, quantidade))

    return "Captura registrada com sucesso."


def exibir_historico():
    """Exibe todas as capturas já registradas"""
    if not historico_capturas:
        return "Histórico de capturas está vazio."

    historico_formatado = [
            f"Pokémon: {nome} - Quantidade capturada: {quantidade}"
            for nome, quantidade in historico_capturas
    ]

    return "\n".join(historico_formatado)


def sair():
    """Exibe uma mensagem de encerramento do programa"""
    print("Saindo do programa...")


def main():
    """Executa o menu principal, até que o usuário escolha sair"""
    # Mantém o menu em loop até que a opção "sair" seja escolhida
    while True:
        for item in menu_info:
            print(item)

        opcao = input("Escolha uma das opções: ").strip()

        # Cada uma das opções chama uma função
        # correspondente à operação escolhida
        # As entradas numéricas são convertidas e validadas
        if opcao == "1":
            nome = input("Digite o nome do Pokémon a ser adicionado: ").strip()
            tipo = input("Digite o tipo do Pokémon a ser adicionado: ").strip()

            if not nome or not tipo:
                print("Erro: o nome e o tipo não podem estar vazios.")
                continue

            try:
                nivel = int(input(
                    "Digite o nível do Pokémon a ser adicionado: "
                ))
                print(adicionar_pokemon(nome, tipo, nivel))
            except ValueError:
                print("Erro: digite um número inteiro para o nível.")
                continue

        elif opcao == "2":
            print(listar_pokemons())

        elif opcao == "3":
            nome = input(
                "Digite o nome do Pokémon a ser removido: "
            )
            print(remover_pokemon(nome))

        elif opcao == "4":
            nome = input(
                "Digite o nome do Pokémon a ser atualizado: "
            )
            try:
                novo_nivel = int(input(
                    "Digite o nível do Pokémon a ser atualizado: "
                ))
                print(atualizar_nivel(nome, novo_nivel))
            except ValueError:
                print("Erro: digite um número inteiro para o nível.")

        elif opcao == "5":
            nome = input(
                "Digite o nome do Pokémon capturado: "
            )
            try:
                quantidade = int(input(
                    "Digite a quantidade de Pokémons capturados: "
                ))
                print(registrar_captura(nome, quantidade))
            except ValueError:
                print("Digite um número inteiro para a quantidade capturada.")

        elif opcao == "6":
            print(exibir_historico())

        elif opcao == "7":
            sair()
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
