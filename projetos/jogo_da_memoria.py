# ----- FUNÇÃO DE JOGO DA MEMÓRIA ----- #
from random import sample


def criar_matriz():
    """
    Cria e retorna uma matriz 4x4 com números de 1 a 8, onde cada número aparece exatamente duas vezes.

    Returns:
    list[list[str]]: Matriz 4x4 do jogo.
    """
    numeros = sample([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8], 16)
    for i in range(16):
        numeros[i] = str(numeros[i])
    matriz = [numeros[:4], numeros[4:8], numeros[8:12], numeros[12:]]
    return matriz


def imprimir_mascara(mascara):
    """
    Imprime a máscara formatada.

    Parameters:
    mascara (list): A máscara a ser impressa.

    Returns:
    None
    """
    print("\033[1m\033[34m  0 1 2 3\033[0m")
    for i in range(4):
        linha = " ".join(mascara[i])
        print(f"\033[1m\033[34m{i}\033[0m {linha}")


def criar_mascara():
    """
    Cria e retorna uma matriz 4x4 com traços, representando a máscara do jogo da memória.

    Returns:
    list[list[str]]: Máscara 4x4 do jogo.
    """
    mascara = [["-" for _ in range(4)] for _ in range(4)]
    return mascara


def validar_posicao(x, y, abertas):
    """
    Valida se a posição fornecida é válida para o jogo da memória.

    Parameters:
    x (int): A coluna da posição a ser validada.
    y (int): A linha da posição a ser validada.
    abertas (list): A lista de posições já abertas.

    Returns:
    bool: True se a posição for válida, False caso contrário.
    """
    if 0 <= x < 4 and 0 <= y < 4:
        if (x, y) not in abertas:
            return True
        else:
            print("\033[1m\033[31mPosição ja aberta!\033[0m")
            return False
    else:
        print("\033[1m\033[31mPosição inválida!\033[0m")
        return False


def entrada_posicao(abertas):
    """
    Solicita ao usuário que insira uma posição válida para o jogo da memória.

    Parameters:
    abertas (list): A lista de posições já abertas.

    Returns:
    tuple: A posição inserida pelo usuário, no formato (x, y).
    """
    while True:
        x, y = input("Escolha uma posição [x y]: ").split()
        x, y = int(x), int(y)
        if validar_posicao(x, y, abertas):
            return x, y


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- JOGO DA MEMÓRIA ----- #
    print("\n\033[1mJogo da Memória\033[0m")
    matriz = criar_matriz()
    mascara = criar_mascara()
    abertas = []
    jogadas = 0
    while mascara != matriz:
        imprimir_mascara(mascara)
        x1, y1 = entrada_posicao(abertas)
        mascara[y1][x1] = matriz[y1][x1]
        imprimir_mascara(mascara)
        x2, y2 = entrada_posicao(abertas + [(x1, y1)])
        mascara[y2][x2] = matriz[y2][x2]
        jogadas += 1
        imprimir_mascara(mascara)
        if matriz[y1][x1] == matriz[y2][x2]:
            abertas.append((x1, y1))
            abertas.append((x2, y2))
            print("Parabéns! Você acertou!")
        else:
            mascara[y1][x1] = "-"
            mascara[y2][x2] = "-"
            print("Você errou... Tente de novo.")
    print(f"\n\033[1mParabéns! Você venceu em {jogadas} jogadas!\033[0m")
