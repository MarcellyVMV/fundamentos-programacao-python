# 8. Defina uma função que, dado o valor da conta de um restaurante, calcule a gorjeta do garçom, considerando que a gorjeta deve ser 15% do valor da conta.


def gorjeta(conta):
    """
    Calcula a gorjeta do garçom a partir do valor da conta.

    Parameters:
    conta (float): Valor da conta do restaurante

    Returns:
    gorjeta (float): Valor da gorjeta
    """
    gorjeta = conta * 0.15
    return gorjeta


# 9. Defina uma nova função que, dado o valor da conta de um restaurante e a porcentagem exigida pela legislação para a gorjeta, calcule o valor dessa gorjeta.


def gorjeta_legislacao(conta, porcentagem):
    """
    Calcula a gorjeta do garçom a partir do valor da conta e da porcentagem exigida pela legislação.

    Parameters:
    conta (float): Valor da conta do restaurante
    porcentagem (float): Porcentagem exigida pela legislação para a gorjeta

    Returns:
    gorjeta_legislacao (float): Valor da gorjeta
    """
    # Digitar a porcentagem como um número inteiro. Exemplo: 10 = 10%.
    gorjeta_legislacao = conta * (porcentagem / 100)
    return gorjeta_legislacao


# 10. Defina uma função que calcule o saldo final de uma conta, dado o saldo inicial, o número de meses e a taxa de juros mensal (juros simples).


def saldo_final(capital, taxa, tempo):
    """
    Calcula o saldo final de uma conta a partir do saldo inicial, da taxa de juros mensal e do número de meses.

    Parameters:
    capital (float): Saldo inicial da conta
    taxa (float): Taxa de juros mensal
    tempo (int): Número de meses

    Returns:
    saldo_final (float): Saldo final da conta
    """
    # Digitar a taxa como um número inteiro. Exemplo: 5 = 5%. e o tempo em meses inteiros. Exemplo: 12 = 12 meses.
    saldo_final = capital * (1 + (taxa / 100) * tempo)
    return saldo_final


# 11. Defina uma função que calcule a distância que a correnteza arrasta um barco que atravessa um rio.


def arrasta(vel_correnteza, largura, vel_barco):
    """
    Calcula a distância que a correnteza arrasta um barco que atravessa um rio.

    Parameters:
    vel_correnteza (float): Velocidade da correnteza
    largura (float): Largura do rio
    vel_barco (float): Velocidade do barco

    Returns:
    arrasta (float): Distância que a correnteza arrasta o barco
    """
    # Digitar na mesma unidade. Exemplo: Se vel_correnteza for em m/s, a largura deve ser em m e a vel_barco em m/s.
    arrasta = vel_correnteza * (largura / vel_barco)
    return arrasta


# test
print("\n\033[1mTest Aplicações\033[0m")

print("\nGorjeta (100) =", gorjeta(100))  # 15
print("Gorjeta (500) =", gorjeta(500))  # 75

print("\nGorjeta Legislação (100, 15) =", gorjeta_legislacao(100, 15))  # 15
print("Gorjeta Legislação (200, 20) =", gorjeta_legislacao(200, 20))  # 40
print("Gorjeta Legislação (500, 30) =", gorjeta_legislacao(500, 30))  # 150

print("\nSaldo Final (1000, 5, 12) =", saldo_final(1000, 5, 12))  # 1600
print("Saldo Final (1000, 5, 24) =", saldo_final(1000, 5, 24))  # 2200
print("Saldo Final (1000, 5, 36) =", saldo_final(1000, 5, 36))  # 2800

print("\nArrasta (1, 1, 1) =", arrasta(1, 1, 1))  # 1
print("Arrasta (2, 2, 2) =", arrasta(2, 2, 2))  # 2
print("Arrasta (3, 3, 3) =", arrasta(3, 3, 3))  # 3
