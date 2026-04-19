# 3. Imagine que você quer enviar uma mensagem de felicitações e gostaria de repetir essas felicitações muitas vezes na mensagem.
def loop_frase(texto, n=1):
    """
    Imprime uma frase repetida um número específico de vezes.

    Parameters:
    texto (string): Frase a ser impressa
    n (int): Quantidade de vezes que a frase deve ser impressa

    Returns:
    None
    """
    for x in range(n):
        print(texto)


# 4. Defina uma função em Python que receba como entrada três números inteiros representando, respectivamente, dia, mês e ano. Sua função deve retornar uma única sequência de caracteres com estas informações formatadas no padrão usual de notação de datas: "dia/mês/ano".
def formatar_data(dia, mes, ano):
    """
    Formata uma data.

    Parameters:
    dia (int): Dia
    mes (int): Mês
    ano (int): Ano

    Returns:
    data (string): Data formatada
    """
    data = f"{dia:02d}/{mes:02d}/{ano}"
    return data


# test
print("\n\033[1mTest Strings\033[0m")

print("\nLoop frase:")
loop_frase("Oi", 3)

print("\nData formatada (1,2,2024) =", formatar_data(1, 2, 2024))  # 01/02/2024
