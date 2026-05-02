# ----- FUNÇÃO DE MENU OPERAÇÕES ----- #


# 2. Escrever um programa que lê um código i, em um intervalo de 1 a 4, e 3 valores a, b, c inteiros e positivos, com a < b. (...)
def menu_operacoes(i, a=0, b=0, c=0):
    """
    Função que realiza operações com base no código de operação fornecido.

    Parameters:
    i (int): Código de operação
    a (int): Primeiro valor
    b (int): Segundo valor
    c (int): Terceiro valor

    Returns:
    float or None: Resultado da operação realizada ou mensagem de erro se os valores forem inválidos.
    """
    if a <= 0 or b <= 0 or c <= 0:
        print("Os valores devem ser positivos.")
        return None
    if a >= b:
        print("O valor de a deve ser menor que b.")
        return None
    if i == 1:
        area = (a + b) * c / 2
        print(f"A área do trapézio é: {area}")
        return area
    elif i == 2:
        a2 = a * a
        b2 = b * b
        c2 = c * c
        print(f"O quadrado desses números é a = {a2}, b = {b2} e c = {c2}")
        return a2, b2, c2
    elif i == 3:
        media = (a + b + c) / 3
        print(f"A média Aritmética é {media}")
        return media
    elif i == 4:
        soma = sum(range(a, b + 1, c))
        print(f"A soma é {soma}")
        return soma
    else:
        print("Código de operação inválido. Digite um número entre 1 e 4.")
        return None


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE MENU OPERAÇÕES ----- #
    i = int(input("Digite o código da operação (1-4): "))
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    menu_operacoes(i, a, b, c)
