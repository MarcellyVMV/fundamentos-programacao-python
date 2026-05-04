# ----- FUNÇÃO DE MATRIZES ----- #


# 1. Escreva uma função que calcule e retorne a matriz resultante da multiplicação de uma matriz por um número.
def mult_matriz(matriz, num=2):
    """
    Calcula e retorna a matriz resultante da multiplicação de uma matriz por um número.

    Parameters:
    matriz (tuple): A matriz a ser multiplicada.
    num (int, optional): O número por qual a matriz deve ser multiplicada. Padrão é 2.

    Returns:
    tuple: A matriz resultante da multiplicação.
    """
    resultado = []
    for line in matriz:
        mult_i = []
        for i in line:
            mult_i.append(i * num)
        resultado.append(tuple(mult_i))
    return tuple(resultado)


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE MATRIZES ----- #
    print("\n\033[1mTest Matrizes\033[0m")
    matriz = (
        (1, 2),
        (3, 4),
    )

    print("\nMatriz = ", matriz)
    print("Matriz * 2 = ", mult_matriz(matriz))  # padrão = 2
    print("\nMatriz * 3 = ", mult_matriz(matriz, 3))
    print("Matriz * 5 = ", mult_matriz(matriz, 5))
