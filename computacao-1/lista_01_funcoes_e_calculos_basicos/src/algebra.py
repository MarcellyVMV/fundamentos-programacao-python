# 4. Termine o desenvolvimento da função que calcula a média de dois números.
def media(num1, num2):
    """
    Calcula a média de dois números.

    Parameters:
    num1 (float): Primeiro número
    num2 (float): Segundo número

    Returns:
    media (float): Média dos dois números
    """
    media = (num1 + num2) / 2
    return media


# 5. Defina uma função que calcule a ordenada de uma função de segundo grau dados os parâmetros a, b, c e a abscissa.
def ordenada(a, b, c, x):
    """
    Calcula a ordenada de uma função de segundo grau dados os parâmetros a, b, c e a abscissa.

    Parameters:
    a (float): Primeiro parâmetro
    b (float): Segundo parâmetro
    c (float): Terceiro parâmetro
    x (float): Abscissa

    Returns:
    ordered (float): Ordenada
    """
    ordered = (a * (x**2)) + (b * x) + c
    return ordered


# 6. Defina uma função que calcule a média ponderada de dois números com os respectivos pesos.
def media_ponderada(num1, peso1, num2, peso2):
    """
    Calcula a média ponderada de dois números com seus respectivos pesos.

    Parameters:
    num1 (float): Primeiro número
    peso1 (float): Peso do primeiro número
    num2 (float): Segundo número
    peso2 (float): Peso do segundo número

    Returns:
    media (float): Média ponderada
    """
    media = (num1 * peso1 + num2 * peso2) / (peso1 + peso2)
    return media


# 7. Defina uma função que calcule o erro entre o valor da soma de uma PG infinita a partir de 1.0 e a soma dos n primeiros termos dessa PG.
def infinite_PG(q, a1=1.0):
    """
    Calcula a soma de uma PG infinita a partir de 1.0.

    Parameters:
    q (float): Razão da PG
    a1 (float): Primeiro termo da PG

    Returns:
    infinite_PG (float): Soma da PG infinita
    """
    infinite_PG = a1 / (1.0 - q)
    return infinite_PG


def finite_PG(q, n, a1=1.0):
    """Calcula a soma dos n primeiros termos de uma PG.

    Parameters:
    q (float): Razão da PG
    n (int): Número de termos
    a1 (float): Primeiro termo da PG

    Returns:
    finite_PG (float): Soma dos n primeiros termos
    """
    finite_PG = a1 * (1.0 - q**n) / (1.0 - q)
    return finite_PG


def error_PG(q, n, a1=1.0):
    """
    Calcula o erro entre a soma de uma PG infinita e a soma dos n primeiros termos.

    Parameters:
    q (float): Razão da PG
    n (int): Número de termos
    a1 (float): Primeiro termo da PG

    Returns:
    error_PG (float): Erro entre as somas
    """
    if q < 0 or q >= 1:  # Verifica se a razão da PG é válida: q ∈ [0, 1)
        return "A razão da PG deve ser maior ou igual a 0 e menor que 1."
    elif n <= 0:  # Verifica se o número de termos é válido: n > 0
        return "O número de termos deve ser maior que 0."
    else:
        error_PG = infinite_PG(q, a1) - finite_PG(q, n, a1)
        return error_PG


# test
print("\n\033[1mTest Álgebra\033[0m")

print("\nMédia (-5, 7) =", media(-5, 7))  # 1
print("Média (-2, 2) =", media(-2, 2))  # 0
print("Média (5, 5) =", media(5, 5))  # 5
print("Média (3, 4) =", media(3, 4))  # 3.5
print("Média (3.0, 4.0) =", media(3.0, 4.0))  # 3.5

print("\nOrdenada (1, 2, 3, 4) =", ordenada(1, 2, 3, 4))  # 27
print("Ordenada (4, 5, 6, 7) =", ordenada(4, 5, 6, 7))  # 237

print("\nMédia Ponderada (2, 3, 4, 5) =", media_ponderada(2, 3, 4, 5))  # 3.25
print("Média Ponderada (4, 5, 6, 7) =", media_ponderada(4, 5, 6, 7))  # 5.17

print("\nErro PG (0.5, 10) =", error_PG(0.5, 10))  # 0.002
print(
    "Erro PG (0.5, 10) =", error_PG(2.0, 50)
)  # A razão da PG deve ser maior ou igual a 0 e menor que 1.
