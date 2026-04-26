# 2. Defina uma função que recebe uma tabela de pontos por time de um campeonato de futebol e fornece a lista com os nomes dos times do campeonato, a pontuação do time campeão, e a média de pontos por time.
campeonato = {}


# -----MAIN-----
def receber_tabela():
    q = int(input("Quantos times jogaram no campeonato? "))
    for x in range(q):
        time = input(f"Digite o nome do {x+1}º time: ")
        notas = input("Digite as notas separadas por espaços: ")
        list_notas = [int(val) for val in notas.split()]
        media = sum(list_notas) / len(list_notas)
        campeonato[time] = {"Pontuação": list_notas, "Média": media}
    exibir_tabela()


# -----PRINT-----
def exibir_tabela():
    x = 0
    print(f"\n Índice | {'Time':^20} | {'Pontuação':^15} | {'Média':^10}")
    print("-------------------------------------------------------------")
    for time, infor in campeonato.items():
        string = str(infor["Pontuação"])
        pontuacao = string[1:-1]
        media = infor["Média"]
        x += 1
        print(f"{x:^7} | {time:^20} | {pontuacao:^15} | {media:^10.2f}")
    print("-------------------------------------------------------------")


# -----EXEC-----
receber_tabela()
