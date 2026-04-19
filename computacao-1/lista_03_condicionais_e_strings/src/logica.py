# 1. Defina uma função que retorne o valor absoluto de um número fornecido.
def absoluto(n):
    """
    Calcula o valor absoluto de um número.

    Parameters:
    n (float): Número

    Returns:
    n (int): Valor absoluto do número
    """
    if n >= 0:
        return n
    elif n < 0:
        return -n
    else:
        return "Digite um número racional"


# 2. Defina uma função que retorne quantas (uma, duas ou nenhuma) são as raízes reais de uma equação de segundo grau, dados os valores dos três coeficientes.
def discriminante(a, b, c):
    """
    Calcula o discriminante (delta) de um polinômio do segundo grau.

    Parameters:
    a (float): Primeiro coeficiente
    b (float): Segundo coeficiente
    c (float): Terceiro coeficiente

    Returns:
    delta (float): Discriminante
    """
    delta = b**2 - 4 * a * c
    return delta


def quantidade_raizes(a, b, c):
    """
    Calcula a quantidade de raízes reais de um polinômio do segundo grau.

    Parameters:
    a (float): Primeiro coeficiente
    b (float): Segundo coeficiente
    c (float): Terceiro coeficiente

    Returns:
    (string): Quantidade de raízes reais
    """
    if a == 0:
        return "A equação não é do segundo grau"
    delta = discriminante(a, b, c)
    if delta > 0:
        return "Essa equação possui 2 raízes reais"
    elif delta == 0:
        return "Essa equação possui 1 raiz real"
    else:
        return "Essa equação não possui raiz real"


# 5. Defina uma função em Python que tenha o comportamento da função matemática da figura abaixo para valores de entrada maiores ou iguais a zero. Para valores negativos o valor da função é sempre zero.
def funcao_q5(x):
    """
    Calcula o valor da função definida na questão 5.

    Parameters:
    x (float): Valor de entrada

    Returns:
    y (float): Valor da função
    """
    if x >= 0 and x < 2:
        y = x
    elif x >= 2 and x <= 3.5:
        y = 2
    elif x > 3.5 and x < 5:
        y = 3
    elif x >= 5:
        y = x**2 - 10 * x + 28
    else:
        y = 0
    return y


# 6. (a) uma função que calcule e retorne o valor do desconto de imposto de INSS
def desconto_INSS(salBruto):
    """
    Calcula o valor do desconto de INSS com base no salário bruto.

    Parameters:
    salBruto (float): Salário bruto

    Returns:
    desconto (float): Desconto de INSS
    """
    if salBruto >= 0 and salBruto <= 2000:
        desconto = salBruto * 0.06
    elif salBruto > 2000 and salBruto <= 3000:
        desconto = salBruto * 0.08
    elif salBruto > 3000:
        desconto = salBruto * 0.1
    else:
        return "Digite seu salário (Inteiro Positivo), não o que sobra no fim do mês"
    return desconto


# 6. (b) uma função que calcule e retorne o valor do desconto de IR
def desconto_IR(salBruto):
    """
    Calcula o valor do desconto de IR com base no salário bruto.

    Parameters:
    salBruto (float): Salário bruto

    Returns:
    desconto (float): Desconto de IR
    """
    if salBruto >= 0 and salBruto <= 2500:
        desconto = salBruto * 0.11
    elif salBruto > 2500 and salBruto <= 5000:
        desconto = salBruto * 0.15
    elif salBruto > 5000:
        desconto = salBruto * 0.22
    else:
        return "Digite seu salário (Inteiro Positivo), não o que sobra no fim do mês"
    return desconto


# 6. (c) uma função que calcule e retorne o salário líquido
def salario_liquido(salBruto):
    """
    Calcula o salário líquido a partir do salário bruto, considerando os descontos de INSS e IR.

    Parameters:
    salBruto (float): Salário bruto

    Returns:
    salLiquido (float): Salário líquido
    """
    if salBruto < 0:
        return "Digite seu salário (Inteiro Positivo), não o que sobra no fim do mês"
    descontos = desconto_INSS(salBruto) + desconto_IR(salBruto)
    salLiquido = salBruto - descontos
    return salLiquido


# test
print("\n\033[1mTest Condicionais/Lógica\033[0m")

print("\nAbsoluto (5) =", absoluto(5))  # 5
print("Absoluto (-5) =", absoluto(-5))  # 5
print("Absoluto (-2.7) =", absoluto(-2.7))  # 2.7

print("\nQuantidade de raízes (1, -3, 2) =", quantidade_raizes(1, -3, 2))  # 2 raízes
print("Quantidade de raízes (1, 2, 1) =", quantidade_raizes(1, 2, 1))  # 1 raiz
print("Quantidade de raízes (1, 0, 1) =", quantidade_raizes(1, 0, 1))  # nenhuma
print("Quantidade de raízes (0, 2, 1) =", quantidade_raizes(0, 2, 1))  # não é 2º grau

print("\nFunção q5 (-1) =", funcao_q5(-1))  # 0
print("Função q5 (1) =", funcao_q5(1))  # 1
print("Função q5 (2.5) =", funcao_q5(2.5))  # 2
print("Função q5 (4) =", funcao_q5(4))  # 3
print("Função q5 (6) =", funcao_q5(6))  # 4

print("\nINSS (2000) =", desconto_INSS(2000))  # 120
print("INSS (2500) =", desconto_INSS(2500))  # 200
print("INSS (4000) =", desconto_INSS(4000))  # 400

print("\nIR (2000) =", desconto_IR(2000))  # 220
print("IR (3000) =", desconto_IR(3000))  # 450
print("IR (6000) =", desconto_IR(6000))  # 1320

print("\nSalário líquido (2000) =", salario_liquido(2000))  # 1660
print("Salário líquido (4000) =", salario_liquido(4000))  # 3000
