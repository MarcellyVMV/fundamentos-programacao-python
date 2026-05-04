# ----- FUNÇÕES DE CONTATINHOS ----- #


# 1. Um aplicativo de agenda de telefones chamado contatinhosApp está sendo desenvolvido em Python por uma equipe. (...)
def print_contato(contato):
    """
    Imprime as informações de um contato específico.

    Parameters:
    contato (list): O contato a ser impresso.

    Returns:
    None
    """
    print(f"\n\033[1m Contato: {contato[0]}\033[0m")
    print(f"{'Índice':^10}|{'Informação':^25}")
    print("-" * 37)
    for i in range(len(contato)):
        if i == 1:
            info = ", ".join(contato[i])
        else:
            info = str(contato[i])
        print(f"{i:^10}|{info:^25}")
    print("-" * 37)


# (a) Criar um contato novo: sua função deve criar e retornar uma lista com as informações do contato. (...)
def criar_contato(nome: str, telefone="", email: str = "", instagram: str = ""):
    """
    Cria um novo contato.

    Parameters:
    nome (str): O nome do contato a ser criado.
    telefone (str, optional): O telefone do contato. Padrão é ''
    email (str, optional): O email do contato. Padrão é ''
    instagram (str, optional): O Instagram do contato. Padrão é ''

    Returns:
    list: O contato criado.
    """
    if telefone != "":
        telefones = [telefone]
    else:
        telefones = []
    contato = [nome, telefones, email, instagram]
    contatos.append(contato)
    print(f"\n\033[1mContato {contato[0]} criado.\033[0m")
    return contato


# (b) Atualizar um contato. Isso significa adicionar ou modificar informações de um contato existente. (...)
def att_contato(contato, index, info):
    """
    Atualiza as informações de um contato existente.

    Parameters:
    contato (list): O contato a ser atualizado.
    index (int): O índice do contato a ser atualizado.
    info (str): A nova informação do contato.

    Returns:
    bool: True se a atualização for bem-sucedida, False caso contrário.
    """
    if index < 0 or index > 3:
        print("\033[1m\nÍndice inválido.\033[0m")
        return False
    elif index == 1:
        if info not in contato[1]:
            contato[1].append(info)
        else:
            print("\033[1mTelefone já cadastrado.\033[0m")
            return False
    else:
        contato[index] = info
    print(f"\n\033[1mContato {contato[0]} atualizado.\033[0m")
    return True


# (c) Excluir telefone. Isso significa modificar informações de um contato existente. Será passado como entrada a lista com as informações atuais de um contato, e o telefone que se deseja excluir:
def excluir_telefone(contato, telefone):
    """
    Exclui um telefone de um contato existente.

    Parameters:
    contato (list): O contato do qual excluir o telefone.
    telefone (str): O telefone a ser excluído.

    Returns:
    bool: True se a exclusão for bem-sucedida, False caso contrário.
    """
    if telefone in contato[1]:
        contato[1].remove(telefone)
        print(f"\n\033[1mTelefone {telefone} excluído do contato {contato[0]}.\033[0m")
        return True
    else:
        print(
            f"\n\033[1mTelefone {telefone} não encontrado no contato {contato[0]}.\033[0m"
        )
        return False


# (d) Buscar os dados de um contato salvo: sua função recebe como entrada a lista de contatos e uma string referente ao nome buscado, e deve retornar uma lista de contatos que tem o nome buscado.
def buscar_contato(contatos, nome):
    """
    Busca os dados de um contato salvo.

    Parameters:
    contatos (list): A lista de contatos.
    nome (str): O nome do contato a ser buscado.

    Returns:
    list: Uma lista de contatos que tem o nome buscado.
    """
    resultados = []
    for contato in contatos:
        if nome.lower() in contato[0].lower():
            resultados.append(contato)
    return resultados


# (e) Nesta semana, sua tarefas é desenvolver a funcionalidade ”quem ligou”, ou seja, dado um número de telefone, faça uma função que retorne a lista com os dados do contatinho que tem aquele número.
def quem_ligou(contatos, telefone):
    """
    Retorna a lista com os dados do contatinho que tem o número de telefone dado.

    Parameters:
    contatos (list): A lista de contatos.
    telefone (str): O número de telefone a ser buscado.

    Returns:
    list: A lista com os dados do contatinho que tem o número de telefone dado, ou uma lista vazia se não encontrado.
    """
    resultados = []
    for contato in contatos:
        if telefone in contato[1]:
            resultados.append(contato)
    return resultados


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE CONTATINHOS ----- #
    contatos = []
    bruno = criar_contato(
        "Bruno Campos",
        "2199112233",
        "brunoc91@email.com",
        "@brunocampos91",
    )
    marcelly = criar_contato("Marcelly", "21911112222", "marcelly@email.com")

    print_contato(bruno)
    print_contato(marcelly)

    att_contato(marcelly, 3, "@marcelly")
    att_contato(bruno, 1, "2133992211")
    att_contato(bruno, 5, "NDA")  # Teste de índice inválido
    att_contato(bruno, 1, "2133992211")  # Teste de telefone já cadastrado

    excluir_telefone(bruno, "2199112233")
    excluir_telefone(bruno, "0000000000")  # Teste de telefone inválido
    excluir_telefone(marcelly, "21911112222")

    marcello = criar_contato("Marcello", "21912345678")

    print(buscar_contato(contatos, "Bruno"))
    print(buscar_contato(contatos, "Marcel"))
    print(buscar_contato(contatos, "Maria"))  # Teste de contato inexistente

    att_contato(marcelly, 1, "21912345678")

    print(quem_ligou(contatos, "2199112233"))
    print(quem_ligou(contatos, "21912345678"))
