# ----- FUNÇÃO DE AFINIDADE ----- #


# 2. Afinidades entre pessoas podem ser descritas através de dicionários. (...) Escreva uma fun ̧c ̃ao chamada deu match que recebe um dicionário de afinidades com mapeamentos de strings em listas de strings, e retorna uma lista de tuplas com afinidade mútua, ou seja, em que ambos se curtiram. (...)
def deu_match(afinidades: dict):
    """
    Retorna uma lista de tuplas com afinidade mútua, ou seja, em que ambos se curtiram.

    Parameters:
    afinidades (dict): Um dicionário de afinidades com mapeamentos de strings em listas de strings.

    Returns:
    list: Uma lista de tuplas com afinidade mútua, ou seja, em que ambos se curtiram.
    """
    matches = []
    for pessoa, curtidas in afinidades.items():
        for curtida in curtidas:
            if pessoa in afinidades.get(curtida, []):
                match = tuple(sorted((pessoa, curtida)))
                if match not in matches:
                    matches.append(match)
    return matches


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE DEU MATCH ----- #
    print("\n\033[1mTeste Afinidades\033[0m")
    afinidades = {
        "Leo": ["Sofia", "Andrea", "Bia"],
        "Marcos": ["Andrea", "Bia"],
        "Sofia": ["Leo"],
        "Alex": ["Andrea", "Marcos"],
        "Andrea": ["Marcos"],
        "Bia": ["Sofia"],
    }
    print("Matches =", deu_match(afinidades))
    # [('Leo', 'Sofia'), ('Andrea', 'Marcos')]
