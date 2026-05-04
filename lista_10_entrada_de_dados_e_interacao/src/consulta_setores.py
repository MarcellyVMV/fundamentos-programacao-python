# ----- FUNÇÃO DE CONSULTA DE SETORES ----- #


# 3. (...) Escreva uma função que receba uma matriz como a do exemplo e faça uma busca por setor, ou seja, dado um nome de um setor da empresa, a função retorna os dados de todos os funcionários daquele setor. (...)
def buscarSetor(funcionarios, setor):
    """
    Função que busca funcionários de um setor específico.

    Parameters:
    funcionarios (list): Lista de funcionários.
    setor (str): Setor a ser buscado.

    Returns:
    list: Lista de funcionários do setor buscado.
    """
    retorno = []
    for empregado in funcionarios:
        if setor.lower() == empregado[2].lower():
            retorno.append([empregado[0], empregado[1], empregado[3]])
    if len(retorno) == 0:
        return "Nenhum registro encontrado."
    else:
        return retorno


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE CONSULTA DE SETORES ----- #
    funcionarios = [
        ["Adalberto Ferreira", "1091982", "Contabilidade", "(21) 99281-2983"],
        ["Juliana Vasconcelos", "1111722", "Recursos Humanos", "(21) 99848-1902"],
        ["Flavia Amorim", "01128938", "Contabilidade", "(22) 99273-9404"],
    ]

    print("\n\033[1mTest Consulta Setores\033[0m")
    setor = input("Buscar funcionários do setor: ")
    print(buscarSetor(funcionarios, setor))
