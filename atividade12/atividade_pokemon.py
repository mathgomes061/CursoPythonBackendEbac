import asyncio
import random
import time

# Listas contendo os possíveis Pokémons encontrados em cada região
lista_pokemons_kanto = ["Bulbassauro", "Charmander", "Squirtle"]
lista_pokemons_johto = ["Chikorita", "Cyndaquill", "Totodile"]
lista_pokemons_hoenn = ["Treecko", "Torchic", "Mudkip"]


# Funções assíncronas responsáveis por selecionar um Pokémon
# aleatório de sua respectiva lista, após aguardar um tempo aleatório
async def busca_pokemon_kanto():
    await asyncio.sleep(random.uniform(1, 5))
    pokemon_kanto = random.choice(lista_pokemons_kanto)
    return pokemon_kanto


async def busca_pokemon_johto():
    await asyncio.sleep(random.uniform(1, 5))
    pokemon_johto = random.choice(lista_pokemons_johto)
    return pokemon_johto


async def busca_pokemon_hoenn():
    await asyncio.sleep(random.uniform(1, 5))
    pokemon_hoenn = random.choice(lista_pokemons_hoenn)
    return pokemon_hoenn


# Função principal responsável por registrar o tempo total das buscas e
# registrar os Pokémons em uma lista
async def main():
    tempo_inicial = time.perf_counter()
    resultado_buscas = await asyncio.gather(
        busca_pokemon_kanto(),
        busca_pokemon_johto(),
        busca_pokemon_hoenn(),
    )
    tempo_final = time.perf_counter()

    tempo_total = tempo_final - tempo_inicial

    return (
        f"Pokémon de Kanto: {resultado_buscas[0]}\n"
        f"Pokémon de Johto: {resultado_buscas[1]}\n"
        f"Pokémon de Hoenn: {resultado_buscas[2]}\n"
        f"Tempo de execução das buscas: {tempo_total:.2f} segundos"
    )

# Execução e exibição do programa principal
if __name__ == "__main__":
    resultado = asyncio.run(main())
    print(resultado)
