# ----- FUNÇÕES DE CAMPEONATO ----- #
import math


# 2. Defina uma função que recebe uma tabela de pontos por time de um campeonato de futebol e fornece a lista com os nomes dos times do campeonato, a pontuação do time campeão, e a média de pontos por time.
def analise_campeonato(campeonato):
    """
    Analisa um campeonato de futebol, calculando a média de pontos por time, identificando o campeão e a média geral.

    Parameters:
    campeonato (dict): Um dicionário contendo o nome do time como chave e uma lista de pontos como valor.

    Returns:
    tuple[str, dict, float]: Tupla contendo o nome do time campeão, um dicionário com as médias de pontos por time e a média geral do campeonato.
    """
    medias = calcular_medias(campeonato)
    campeao = max(medias, key=medias.get)
    media_geral = math.fsum(medias.values()) / len(medias)
    return campeao, medias, media_geral


def print_campeonato(campeao, medias, media_geral):
    """
    Imprime as informações do campeonato de futebol, incluindo o campeão, as médias de pontos por time e a média geral.

    Parameters:
    campeao (str): O nome do time campeão.
    medias (dict): Um dicionário contendo o nome do time como chave e a média de pontos como valor.
    media_geral (float): A média geral de pontos por time.

    Returns:
    None
    """
    print(f"\n\033[1mCampeão: {campeao}\033[0m")
    print(f"\033[1mTimes e suas Médias:\033[0m")
    for time in medias:
        print(f"   {time}: {medias[time]:.2f}")

    print(f"\033[1mMédia geral: {media_geral:.2f}\033[0m")
    return


def calcular_medias(campeonato):
    """
    Calcula a média de pontos por time em um campeonato de futebol.

    Parameters:
    campeonato (dict): Um dicionário contendo o nome do time como chave e uma lista de pontos como valor.

    Returns:
    dict: Um dicionário contendo o nome do time como chave e a média de pontos como valor.
    """
    medias = {}
    for time, info in campeonato.items():
        if len(info) == 0:
            medias[time] = 0
        else:
            medias[time] = math.fsum(info) / len(info)
    return medias


# -----EXTRA----- #
def ranking_campeonato(campeonato):
    """
    Calcula o ranking dos times com base na média de pontos.

    Parameters:
    campeonato (dict): Um dicionário contendo o nome do time como chave e uma lista de pontos como valor.

    Returns:
    list[tuple[str, float]]: Uma lista de tuplas contendo o nome do time e a média de pontos, ordenada em ordem decrescente.
    """
    medias = calcular_medias(campeonato)
    ranking = sorted(medias.items(), key=lambda item: item[1], reverse=True)
    return ranking


def print_ranking(ranking):
    """
    Imprime o ranking dos times com base na média de pontos.

    Parameters:
    ranking (list): Uma lista de tuplas contendo o nome do time e a média de pontos.

    Returns:
    None
    """
    print(f"\n\033[1m{'Rank':^10}|{'Time':^15}|{'Média':^10}\033[0m")
    print("-" * 37)
    rank = 1
    for time, media in ranking:
        print(f"{str(rank) + 'º':^10}|{time:^15}|{media:^10.2f}")
        rank += 1
    print("-" * 37)
    print(
        f"\033[1m  Média geral:{math.fsum([media for _, media in ranking]) / len(ranking):>20.2f}\033[0m\n"
    )
    return


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE CAMPEONATO ----- #
    campeonato = {
        "Flamengo": [71, 50, 46],
        "Palmeiras": [65, 39, 45],
        "Fluminense": [66, 45, 42],
        "Vasco": [63, 47, 37],
        "Botafogo": [62, 52, 48],
    }

    print_campeonato(analise_campeonato(campeonato))
    print_ranking(ranking_campeonato(campeonato))
