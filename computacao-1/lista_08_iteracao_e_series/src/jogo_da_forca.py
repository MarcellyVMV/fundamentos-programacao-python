# ----- FUNÇÃO DE MÁSCARA ----- #


# 3. Escreva uma função chamada atualiza mascara que recebe como entrada uma string contendo a palavra secreta, uma lista cujos elementos são os caracteres da máscara atual e uma string com a letra que ele acabou de escolher. Sua função deve atualizar a máscara, colocando a letra escolhida no seu devido lugar (caso esteja na palavra). Se a letra não estiver na palavra, a máscara deve ser retornada sem modificações.
def criar_mascara(palavra):
    """
    Cria a máscara do jogo da forca, onde cada letra da palavra é representada por um traço.

    Parameters:
    palavra (string): A palavra que o jogador deve adivinhar.

    Returns:
    list: A lista que representa a máscara do jogo da forca.
    """
    mascara = []
    for i in range(len(palavra)):
        mascara.append("-")
    return mascara


def att_mascara(palavra, mascara, letra):
    """
    Atualiza a máscara do jogo da forca, colocando a letra escolhida no seu devido lugar (caso esteja na palavra). Se a letra não estiver na palavra, a máscara é retornada sem modificações.

    Parameters:
    palavra (string): A palavra que o jogador deve adivinhar.
    mascara (list): A lista que representa a máscara atual.
    letra (string): A letra escolhida pelo jogador.

    Returns:
    tuple[list, bool]: Uma tupla contendo a máscara atualizada e um booleano indicando se a letra estava na palavra.
    """
    palavra = palavra.lower()
    letra = letra.lower()
    if letra in palavra:
        if palavra.count(letra) == 1:
            indice = palavra.index(letra)
            mascara[indice] = letra
        else:
            indice = palavra.index(letra)
            mascara[indice] = letra
            for _ in range(palavra.count(letra) - 1):
                indice = palavra.index(letra, indice + 1)
                mascara[indice] = letra
        return mascara, True
    else:
        return mascara, False


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE MÁSCARA ----- #
    palavra = "Passaro"  # Palavra que o jogador deve adivinhar sem acentos
    mascara = criar_mascara(palavra)
    while "".join(mascara) != palavra.lower():
        print("\nMáscara atual: ", " ".join(mascara))
        letra = input("Digite uma letra: ")
        mascara, acertou = att_mascara(palavra, mascara, letra)
        if not acertou:
            print("\033[1mEssa letra não está na palavra!\033[0m")
    print("\n\033[1mPalavra completa: \033[0m", "".join(mascara))
    print("\033[1mParabéns! Você ganhou!\033[0m")
