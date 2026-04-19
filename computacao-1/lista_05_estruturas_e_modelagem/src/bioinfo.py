# 2. (...) Com base na tabela (simplificada) de trincas de RNA abaixo, crie uma função que receba uma string de tamanho 9 representando uma molécula de RNA mensageiro válida, segundo essa tabela, e retorne a cadeia de 3 aminoácidos que representam a proteína correspondente.
def traducao_rnaM(RNA: str):
    """
    Traduz uma molécula de RNA mensageiro em uma cadeia de aminoácidos correspondente, de acordo com a tabela de trincas de RNA.

    Parameters:
    RNA (str): Uma string de tamanho 9 representando uma molécula de RNA mensageiro válida.

    Returns:
    amino_acidos (str): A cadeia de aminoácidos correspondente à molécula de RNA fornecida.
    """
    if len(RNA) != 9:
        return "RNA deve ter exatamente 9 caracteres"

    for x in RNA:
        if x not in "AUCG":
            return "RNA deve conter apenas os caracteres A, U, C e G"

    trinca_amino = {
        "UUU": "Phe",
        "CUU": "Leu",
        "UUA": "Leu",
        "AAG": "Lisina",
        "UCU": "Ser",
        "UAU": "Tyr",
        "CAA": "Gln",
    }
    amino_acidos = (
        trinca_amino[RNA[0:3]]
        + "-"
        + trinca_amino[RNA[3:6]]
        + "-"
        + trinca_amino[RNA[6:]]
    )
    return amino_acidos


# test
print("\n\033[1mTest Tradução RNA\033[0m")

print("\nRNA (UUUCUUAAG) =", traducao_rnaM("UUUCUUAAG"))  # Phe-Leu-Lisina
print("RNA (UCUUAUCAA) =", traducao_rnaM("UCUUAUCAA"))  # Ser-Tyr-Gln
print("RNA (UUUUUUUUU) =", traducao_rnaM("UUUUUUUUU"))  # Phe-Phe-Phe
print("RNA (ABC123456) =", traducao_rnaM("ABC123456"))  # erro caracteres inválidos
print("RNA (UUUCUU) =", traducao_rnaM("UUUCUU"))  # erro tamanho
