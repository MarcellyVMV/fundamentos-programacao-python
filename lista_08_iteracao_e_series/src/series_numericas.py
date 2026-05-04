# ----- FUNÇÃO DE SÉRIES NUMÉRICAS ----- #


# 4. (a) Escreva uma função que, dado n, calcule a soma da série até o termo n.
def serie_4pi(n):
    """
    Calcula a soma da série de Leibniz até o termo n.

    Parameters:
    n (int): Número de termos

    Returns:
    float: Soma da série de Leibniz
    """
    soma = 0
    for i in range(n + 1):
        soma += (-1) ** i / (2 * i + 1)
    return soma


# 4. (b) Escreva uma função que calcule a soma da série com erro inferior a 0, 01, ou seja, calcule a soma desta série de modo que |sn−Π/4| < 0, 01. Sua função deve retornar também o número de termos necessários para chegar a este erro, ou seja, sua função retornará uma tupla com os dois valores calculados. Importante: Utilize obrigatoriamente a função definida no item anterior.
from math import pi, fabs


def erro_serie4Pi():
    """
    Calcula a soma da série de Leibniz com erro inferior a 0,01 e o número de termos necessários para chegar a este erro.

    Returns:
    tuple[float, int]: Uma tupla contendo a soma da série de Leibniz com erro inferior a 0,01 e o número de termos necessários para chegar a este erro.
    """
    i = 0
    soma = serie_4pi(i)
    while fabs(soma - (pi / 4)) >= 0.01:
        i += 1
        soma = serie_4pi(i)
    return soma, i


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE SÉRIE NUMÉRICA ----- #
    print("\n\033[1mTest Série de Leibniz\033[0m")

    print("\nSoma até n=0 =", serie_4pi(0))  # 1.0
    print("Soma até n=1 =", serie_4pi(1))  # 0.666...
    print("Soma até n=2 =", serie_4pi(2))  # 0.866...
    print("Soma até n=10 =", serie_4pi(10))  # 0.8080789523513985

    resultado, termos = erro_serie4Pi()

    print("\nSoma com erro < 0.01 =", resultado)  # 0.7953941713587581
    print("Número de termos necessários =", termos)  # 24
    print("π/4 =", pi / 4)  # 0.7853981633974483
