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


# ----- MAIN ----- #
if __name__ == "__main__":
    # ----- TESTE DE CONTATINHOS ----- #
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

    print_contato(bruno)
    print_contato(marcelly)
