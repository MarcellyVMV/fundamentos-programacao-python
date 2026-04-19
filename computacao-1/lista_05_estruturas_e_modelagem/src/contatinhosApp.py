# 1. Um aplicativo de agenda de telefones chamado contatinhosApp está sendo desenvolvido em Python por uma equipe. (...)
contatinhos = {
    "Marcelly": [["971501694"], "marcelly@ufrj", "@marcelly"],
    "Queiroz": [["988887777", "900001111"], "NDA", "@l.queiroz"],
}


# -----MAIN LOOP-----
def contatinhosApp():
    """
    Função principal do aplicativo, onde o usuário pode escolher qual ação deseja realizar.

    Parameters:
    None

    Returns:
    None
    """
    while True:
        indice = input(
            "\nDigite o número da ação que deseja realizar (1-Adicionar, 2-Atualizar, 3-Deletar, 4-Ver, 0-Sair): "
        )
        if indice == "0":
            print("\033[1m\nSaindo...\n\033[0m")
            break
        elif indice == "1":
            nome = input("Digite o nome do Contatinho: ")
            telefone = input("Digite o telefone de " + nome + ": ")
            email = input("Digite o email de " + nome + ": ")
            instagram = input("Digite o instagram " + nome + ": ")
            add_contatinhos(nome, telefone, email, instagram)
        elif indice == "2":
            att_contatinhos()
        elif indice == "3":
            del_contatinhos()
        elif indice == "4":
            print_contatinhos()
        else:
            print("\033[1mOpção inválida\033[0m")


# -----Adicionar contato-----
def add_contatinhos(
    nome: str, telefone="NDA", email: str = "NDA", instagram: str = "NDA"
):
    """
    Adiciona um novo contato à lista de contatinhos.

    Parameters:
    nome (str): O nome do contato a ser adicionado.
    telefone (str, optional): O telefone do contato. Padrão é 'NDA'
    email (str, optional): O email do contato. Padrão é 'NDA'
    instagram (str, optional): O Instagram do contato. Padrão é 'NDA'

    Returns:
    None
    """
    contatinhos[nome] = [[telefone], email, instagram]
    print("\033[1m\nContato adicionado.\n\033[0m")
    return


# -----Atualizar contato-----
def att_contatinhos():
    """
    Atualiza as informações de um contato existente na lista de contatinhos.

    Parameters:
    None

    Returns:
    None
    """
    nome = input("Qual é o nome do contatinho que deseja atualizar? ")
    while True:
        if nome not in contatinhos:
            print("Contato não encontrado")
        else:
            indice = int(
                input(
                    "\nDigite o número da informação que deseja atualizar (1-Nome, 2-Telefone, 3-Email, 4-Instagram, 0-Voltar): "
                )
            )
            if indice == 0:
                return
            elif indice == 1:
                novo_nome = input("Digite o novo nome do Contatinho: ")
                contatinhos[novo_nome] = contatinhos[nome]
                del contatinhos[nome]
                print("\033[1m\nContato atualizado.\n\033[0m")

            elif indice == 2:
                novo_tel = input("Digite o novo telefone do Contatinho: ")
                contatinhos[nome][0].append(novo_tel)
                print("\033[1m\nContato atualizado.\n\033[0m")

            elif indice == 3:
                novo_email = input("Digite o novo email do Contatinho: ")
                contatinhos[nome][1] = novo_email
                print("\033[1m\nContato atualizado.\n\033[0m")

            elif indice == 4:
                novo_insta = input("Digite o novo instagram do Contatinho: ")
                contatinhos[nome][2] = novo_insta
                print("\033[1m\nContato atualizado.\n\033[0m")

            else:
                print("\033[1m\nOpção inválida.\n\033[0m")


# -----Extra-----


# -----Deletar contato-----
def del_contatinhos():
    """
    Deleta um contato da lista de contatinhos.

    Parameters:
    None

    Returns:
    None
    """
    nome = input("\nQual é o nome do contato que deseja deletar? ")
    if nome in contatinhos:
        del contatinhos[nome]
        print("\033[1mContato deletado.\033[0m")
    else:
        print("Contato não encontrado")


# -----Imprimir contatos-----
def print_contatinhos():
    """
    Imprime a tabela de contatinhos formatada.

    Parameters:
    None

    Returns:
    None
    """
    print(
        "\n------------------------------------------------------------------------------------------------"
    )
    print(f'{"Nome":^10} | {"Telefone":^30} | {"E-mail":^15} | {"Instagram":^10}')
    print(
        "------------------------------------------------------------------------------------------------"
    )
    for name, infor in contatinhos.items():
        print(f"{name:^10} | {str(infor[0]):^30} | {infor[1]:^15} | {infor[2]:^10}")
    print(
        "------------------------------------------------------------------------------------------------"
    )


# -----INÍCIO DO PROGRAMA-----
print_contatinhos()
contatinhosApp()
