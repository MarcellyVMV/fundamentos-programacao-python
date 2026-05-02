# ----- FUNÇÃO DE SEQUÊNCIAS ----- #

# 1. Escreva um programa em Python que leia uma série de lançamentos de um dado, guarde-os numa lista, e conte o número de ocorrências de séries de faces repetidas. (...)
from random import randint


def jogadas(n):
    """
    Função que simula n lançamentos de um dado e conta o número de ocorrências de séries de faces repetidas.

    Parameters:
    n (int): Número de lançamentos de um dado.

    Returns:
    int: Número de ocorrências de séries de faces repetidas.
    """
    serie = []
    for i in range(n):
        serie.append(randint(1, 6))
    print("Lançamentos: ", serie)
    repeticoes = 0
    for i in range(1, len(serie)):
        if serie[i] == serie[i - 1]:
            if i == 1 or serie[i - 1] != serie[i - 2]:
                repeticoes += 1
    return repeticoes


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE JOGADAS ----- #
    print("\n\033[1mTest Sequências\033[0m")
    print("\nNúmero de séries =", jogadas(15))
