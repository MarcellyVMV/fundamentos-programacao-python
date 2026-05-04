# ----- FUNÇÕES DE ÁLGEBRA ----- #


# 1. (a) teste as funções max e min no console do Python, digitando, por exemplo:
print("\nmax(3,2.8,3.9) =", max(3, 2.8, 3.9))
print("min(7,2,4,1,0) =", min(7, 2, 4, 1, 0))


# 1. (b) Faça uma função que calcule e retorne a média de três números inteiros.
def media(n1, n2, n3):
    """
    Calcula a média de três números.

    Parameters:
    n1 (int): Primeiro número
    n2 (int): Segundo número
    n3 (int): Terceiro número

    Returns:
    float: Média dos três números
    """
    return (n1 + n2 + n3) / 3


# 1. (c) Faça uma função que retorne, dados três números, a diferença do maior deles com a média (obrigatoriamente use a função desenvolvida no item b).
def diferenca_MaxMed(n1, n2, n3):
    """
    Calcula a diferença do maior deles com a média.

    Parameters:
    n1 (float): Primeiro número
    n2 (float): Segundo número
    n3 (float): Terceiro número

    Returns:
    float: Diferença do maior deles com a média
    """
    diferenca = max(n1, n2, n3) - media(n1, n2, n3)
    return diferenca


# 1. (d) Faça uma função que retorne, dados três números, a soma do menor deles com a média (obrigatoriamente use a função desenvolvida no item b).
def soma_MaxMed(n1, n2, n3):
    """
    Calcula a soma do menor deles com a média.

    Parameters:
    n1 (float): Primeiro número
    n2 (float): Segundo número
    n3 (float): Terceiro número

    Returns:
    float: Soma do menor deles com a média
    """
    soma = min(n1, n2, n3) + media(n1, n2, n3)
    return soma


# 2. (a) faça uma função que dados os coeficientes a, b e c, calcula o discriminante de um polinômio do segundo grau.
def discriminante(a, b, c):
    """
    Calcula o discriminante (delta) de um polinômio do segundo grau.

    Parameters:
    a (float): Primeiro coeficiente
    b (float): Segundo coeficiente
    c (float): Terceiro coeficiente

    Returns:
    float: Discriminante
    """
    delta = b**2 - 4 * a * c
    return delta


# 2. (b) faça uma função que calcule a primeira raiz real de uma equação do segundo grau, dados seus coeficientes a, b e c.
def raiz1(a, b, c):  # Sem math
    """
    Calcula a primeira raiz real de uma equação do segundo grau.

    Parameters:
    a (float): Primeiro coeficiente
    b (float): Segundo coeficiente
    c (float): Terceiro coeficiente

    Returns:
    float: Primeira raiz real
    """
    if a == 0:
        return "Não é equação do segundo grau."
    delta = discriminante(a, b, c)
    if delta >= 0:
        raiz = (-b + (delta) ** (1 / 2)) / (2 * a)
        return raiz
    else:
        return "Essa função não tem raiz real."


# 2. (c) faça uma função que calcule a segunda raiz real de uma equação do segundo grau, dados seus coeficientes a, b e c.
import math


def raiz2(a, b, c):  # Com Math
    """
    Calcula a segunda raiz real de uma equação do segundo grau.

    Parameters:
    a (float): Primeiro coeficiente
    b (float): Segundo coeficiente
    c (float): Terceiro coeficiente

    Returns:
    float: Segunda raiz real
    """
    if a == 0:
        return "Não é equação do segundo grau."
    delta = discriminante(a, b, c)
    if delta >= 0:
        raiz = (-b - math.sqrt(delta)) / (2 * a)
        return raiz
    else:
        return "Essa função não tem raiz real."


# 3. (..) (b) faça uma função para calcular o número de termos dados os valores inicial e final e a razão;
def n_termos(inicial, final, r):
    """
    Calcula o número de termos dados os valores inicial e final e a razão.

    Parameters:
    inicial (float): Valor inicial
    final (float): Valor final
    r (float): Razão

    Returns:
    int: Número de termos
    """
    if r == 0:
        return "A razão deve ser diferente de 0."
    else:
        n = int(((final - inicial) / r) + 1)
        return n


# 3. (c) e outra função para calcular a soma da PA dados os valores inicial, final e a razão.
def soma_PA(inicial, final, r):
    """
    Calcula a soma da PA (Progressão Aritmética) dados os valores inicial e final e a razão.

    Parameters:
    inicial (float): Valor inicial
    final (float): Valor final
    r (float): Razão

    Returns:
    float: Soma da PA
    """
    if r == 0:
        return "A razão deve ser diferente de 0."
    else:
        soma = (final + inicial) * n_termos(inicial, final, r) / 2
        return soma


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE ÁLGEBRA ----- #
    print("\n\033[1mTest Álgebra\033[0m")

    print("\nMédia (1,2,3) =", media(1, 2, 3))  # 2
    print("Média (5,5,5) =", media(5, 5, 5))  # 5

    print("\nDiferença Max - Média (1,2,3) =", diferenca_MaxMed(1, 2, 3))  # 1
    print("Diferença Max - Média (10,5,0) =", diferenca_MaxMed(10, 5, 0))  # 5

    print("\nSoma Min + Média (1,2,3) =", soma_MaxMed(1, 2, 3))  # 3
    print("Soma Min + Média (10,5,0) =", soma_MaxMed(10, 5, 0))  # 5

    print("\nDelta (1, -3, 2) =", discriminante(1, -3, 2))  # 1

    print("\nRaiz1 (1, -3, 2) =", raiz1(1, -3, 2))  # 2
    print("Raiz2 (1, -3, 2) =", raiz2(1, -3, 2))  # 1

    print("\nRaiz1 (1, 0, 1) =", raiz1(1, 0, 1))  # sem raiz real
    print("Raiz2 (1, 0, 1) =", raiz2(1, 0, 1))  # sem raiz real

    print("\nNúmero de termos (1 → 10, r=1) =", n_termos(1, 10, 1))  # 10
    print("Número de termos (2 → 20, r=2) =", n_termos(2, 20, 2))  # 10

    print("\nSoma PA (1 → 10, r=1) =", soma_PA(1, 10, 1))  # 55
    print("Soma PA (2 → 20, r=2) =", soma_PA(2, 20, 2))  # 110

    print("\nNúmero de termos (1 → 10, r=0) =", n_termos(1, 10, 0))  # erro
    print("Soma PA (1 → 10, r=0) =", soma_PA(1, 10, 0))  # erro
