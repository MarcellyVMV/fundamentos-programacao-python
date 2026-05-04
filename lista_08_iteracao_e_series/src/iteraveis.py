# ----- FUNÇÃO DE ITERÁVEIS ----- #


# 1. Defina uma função que dado um valor (iterável) de tipo string, list ou tuple, e um potencial elemento (elem), devolva a quantidade de vezes em que elem aparece em iterável.
def contar(iteravel, elem):
    """
    Conta a quantidade de vezes que um elemento aparece em um iterável.

    Parameters:
    iteravel (iterável): Iterável
    elem (elemento): Elemento a ser contado

    Returns:
    int: Quantidade de vezes que o elemento aparece no iterável
    """
    contagem = 0
    for i in iteravel:
        if i == elem:
            contagem += 1
    return contagem


# 2. Defina uma função que dado um valor (iterável) de tipo string, list ou tuple, um potencial elemento (elem), e dois índices não negativos (ini e fim), devolva a quantidade de vezes em que elem aparece no trecho de iterável limitado por ini (inclusive) e fim (exclusive).
def contar_trecho(iteravel, elem, ini: int, fim: int):
    """
    Conta a quantidade de vezes que um elemento aparece em um trecho de um iterável.

    Parameters:
    iteravel (iterável): Iterável
    elem (elemento): Elemento a ser contado
    ini (int): Indice inicial
    fim (int): Indice final

    Returns:
    int: Quantidade de vezes que o elemento aparece no trecho do iterável
    """
    contagem = 0
    for i in iteravel[ini:fim]:
        if i == elem:
            contagem += 1
    return contagem


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE ITERÁVEIS ----- #
    print("\n\033[1mTest Iteráveis\033[0m")

    print(
        "\nCount string =",
        contar("Seja estranho. Seja aleatório. Seja quem você é.", "a"),
    )  # 6
    print("Count tuple =", contar((1, 2, 0, 3, 1), 1))  # 2
    print("Count list =", contar([5, 7, 5, 9, 5], 5))  # 3

    print(
        "\nCountx string =",
        contar_trecho("Seja estranho. Seja aleatório. Seja quem você é.", "a", 0, 20),
    )  # 3
    print("Countx tuple =", contar_trecho((1, 2, 0, 3, 1), 1, 0, 4))  # 1
    print("Countx list =", contar_trecho([5, 7, 5, 9, 5], 5, 2, 5))  # 2
