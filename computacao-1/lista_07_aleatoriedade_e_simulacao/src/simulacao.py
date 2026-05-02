# ----- FUNÇÃO DE SIMULAÇÃO ----- #

# 1. Faça uma função que simule um jogo de dois dados. A função deve contar quantas vezes os dados foram jogados até que saiam números repetidos. Use a função randint do módulo random para simular a jogada de um dado.
from random import randint


def jogo():
    """
    Simula um jogo de dois dados e conta quantas vezes os dados foram jogados até que saiam números repetidos.

    Returns:
    int: Quantidade de jogadas necessárias para obter números repetidos.
    """
    jogadas = 0
    while True:
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        jogadas += 1
        if dado1 == dado2:
            return jogadas


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE SIMULAÇÃO ----- #
    print("\n\033[1mTest Simulação\033[0m")

    print("\nJogo 1 =", jogo())
    print("Jogo 2 =", jogo())
    print("Jogo 3 =", jogo())
    print("Jogo 4 =", jogo())
    print("Jogo 5 =", jogo())
