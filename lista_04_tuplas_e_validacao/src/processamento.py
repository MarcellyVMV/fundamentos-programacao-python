# ----- FUNÇÕES DE PROCESSAMENTO ----- #


# 1. Faça uma função em Python chamada SIGA, que receba uma tupla contendo 4 informações: o nome do aluno e três notas. (...)
def SIGA(informacao):
    """
    Calcula a média de um aluno e determina sua situação.

    Parameters:
    informacao (tuple): Tupla contendo o nome do aluno e três notas.

    Returns:
    tuple: Tupla contendo o nome do aluno, a média e a situação.
    """
    media = round(
        (float(informacao[1]) + float(informacao[2]) + float(informacao[3])) / 3, 1
    )
    if media >= 7:
        situacao = (informacao[0], media, "Aprovado", "Parabéns")
    elif media >= 5:
        situacao = (informacao[0], media, "Aprovado", "")
    else:
        situacao = (informacao[0], media, "Reprovado", "")
    return situacao


# 2. (…) Faça uma função que receba o ano de nascimento e retorne o signo aproximado correspondente.
def signo_chines(ano):
    """
    Determina o signo chinês com base no ano de nascimento.

    Parameters:
    ano (int): Ano de nascimento

    Returns:
    str: Signo chinês
    """
    signos = (
        "Macaco",
        "Galo",
        "Cão",
        "Porco",
        "Rato",
        "Boi",
        "Tigre",
        "Coelho",
        "Dragão",
        "Serpente",
        "Cavalo",
        "Carneiro",
    )
    return signos[(ano % 12)]


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE PROCESSAMENTO ----- #
    print("\n\033[1mTest Tuplas e Strings\033[0m")

    print(
        "\nSIGA ('Ana', 8, 7, 9) =", SIGA(("Ana", 8, 7, 9))
    )  # ('Ana', 8.0, 'Aprovado', 'Parabéns')
    print(
        "SIGA ('Bruno', 6, 5, 4) =", SIGA(("Bruno", 6, 5, 4))
    )  # ('Bruno', 5.0, 'Aprovado', '')
    print(
        "SIGA ('Carlos', 3, 4, 2) =", SIGA(("Carlos", 3, 4, 2))
    )  # ('Carlos', 3.0, 'Reprovado', '')

    print("\nSigno chinês (2000) =", signo_chines(2000))  # Dragão
    print("Signo chinês (1996) =", signo_chines(1996))  # Rato
    print("Signo chinês (2005) =", signo_chines(2005))  # Galo
    print("Signo chinês (2024) =", signo_chines(2026))  # Cavalo
