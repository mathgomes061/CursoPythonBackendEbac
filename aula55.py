# Dois amigos (Anton e Danik) jogaram n partidas de xadrez
# Nehnuma das partidas terminou em empate
# Determine quem ganhou mais, segundo as informações:

match_numbers = 6
winners = "ADAAAA"

anton_wins = winners.count("A")
danik_wins = winners.count("D")

if anton_wins > danik_wins:
    print(f"Anton ganhou mais partidas. Total de vitórias: {anton_wins}")
else:
    print(f"Danik ganhou mais partidas. Total de vitórias: {danik_wins}")
