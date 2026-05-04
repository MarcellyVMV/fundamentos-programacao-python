# ----- FUNÇÕES DE VALIDAÇÃO ----- #


# 3. (…) Faça uma função que receba como entrada uma string contendo uma sequência de dígitos, que supostamente corresponde ao número de telefone informado por um usuário (…)
def telefone(numero):
    """
    Valida um número de telefone e o formata.

    Parameters:
    numero (str): String contendo a sequência de dígitos do número de telefone.

    Returns:
    tuple: Tupla contendo o código de área e o número formatado.
    """
    if not numero.isdigit():
        return "Número inválido"
    if len(numero) in [10, 11]:
        number = (numero[:2], numero[2:])
    elif len(numero) in [9, 8]:
        number = ("", numero)
    else:
        return "Número inválido"
    return number


# 4. Faça uma função em Python chamada formato data, que receba uma string de 8 posições, referente a uma data, e retorna os possíveis formatos em que a data fornecida possa ser interpretada. (...) assumir que a string de entrada contém duas barras (’/’) nas posições 2 e 5, (...)
def formato_data(data):
    """
    Determina os possíveis formatos de uma data fornecida.

    Parameters:
    data (str): String de 8 posições representando uma data.

    Returns:
    list: Lista contendo os formatos possíveis.
    """
    retornar = []
    if (
        int(data[:2]) != 0
        and int(data[:2]) <= 31
        and int(data[3:5]) != 0
        and int(data[3:5]) <= 12
    ):
        retornar.append("dd/mm/yy")
    if (
        int(data[3:5]) != 0
        and int(data[3:5]) <= 12
        and int(data[6:]) != 0
        and int(data[6:]) <= 31
    ):
        retornar.append("yy/mm/dd")
    if (
        int(data[:2]) != 0
        and int(data[:2]) <= 12
        and int(data[3:5]) != 0
        and int(data[3:5]) <= 31
    ):
        retornar.append("mm/dd/yy")
    return retornar


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE VALIDAÇÃO ----- #
    print("\n\033[1mTest Validação\033[0m")

    print("\nTelefone (21987654321) =", telefone("21987654321"))  # ('21', '987654321')
    print("Telefone (987654321) =", telefone("987654321"))  # ('', '987654321')
    print("Telefone (123) =", telefone("123"))  # inválido
    print("Telefone (21abc123456) =", telefone("21abc123456"))  # inválido

    print(
        "\nFormato data (01/01/26) =", formato_data("01/01/26")
    )  # ['dd/mm/yy', 'yy/mm/dd', 'mm/dd/yy']
    print("Formato data (31/12/99) =", formato_data("31/12/99"))  # ['dd/mm/yy']
    print(
        "Formato data (17/05/24) =", formato_data("17/05/24")
    )  # ['dd/mm/yy', 'yy/mm/dd']
