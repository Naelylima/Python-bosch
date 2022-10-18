def menu_principal ():
    print("************** Bem vindo ao Jogo da Forca ****************")
    print("[1] - X "
          "\n[2] - O"
          "\n[3] - Sair")

def desenho_forca(lista):
    print("┌───┬───┬───┐")
    print(f"│ {lista[0][0]} │ {lista[0][1]} │ {lista[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {lista[1][0]} │ {lista[1][1]} │ {lista[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {lista[2][0]} │ {lista[2][1]} │ {lista[2][2]} │")
    print("└───┴───┴───┘")

def menu_escolha(jogador_1, jogador_2):
    while True:
        try:
            if jogador_1 > 3 or jogador_1 < 1:
                print("Escolha uma opção válida\n")
                break
            if jogador_1 == 1:
                jogador_1 = "X"
                jogador_2 = "O"
                print("-"*38)
                print(f"Jogador 1 neste jogo você será: {jogador_1}\nJogador 2 neste jogo você será: {jogador_2}")
                return jogador_1, jogador_2
            elif jogador_1 == 3:
                print("-" * 38)
                print("        Obrigada por participar!")
                print("-" * 38)
                break
            elif jogador_1 == 2:
                jogador_1 = "O"
                jogador_2 = "X"
                print("-" * 38)
                print(f"Jogador 1 neste jogo você será: {jogador_1}\nJogador 2 neste jogo você será: {jogador_2}")
                return jogador_1, jogador_2
        except ValueError:
            print("Você digitou algo errado\n")
            continue

def jogada(jogada1, jogada2):
    for linha in range(0, 3):
        if jogada1 in lista_posicoes[linha] == "X" or jogada1 in lista_posicoes[linha] == "O":
            print("Esse opção já foi escolhida")
        else:
            if jogada1 in lista_posicoes[linha]:
                posicao = lista_posicoes[linha].index(jogada1)
                lista_posicoes[linha][posicao] = jogador1
                vitoria()
    for linha in range(0, 3):
        if jogada2 in lista_posicoes[linha] == "X" or jogada2 in lista_posicoes[linha] == "O":
            print("Esse opção já foi escolhida")
        else:
            if jogada2 in lista_posicoes[linha]:
                posicao = lista_posicoes[linha].index(jogada2)
                lista_posicoes[linha][posicao] = jogador2
                vitoria()
    desenho_forca(lista_posicoes)

def vitoria():
    for linhas in range(0, 3):
        if lista_posicoes[linhas][0] and lista_posicoes[linhas][1] and lista_posicoes[linhas][2] == jogador1:
            print("Jogador 1, VENCEU")
            venceu= True
            return venceu
        elif lista_posicoes[linhas][0] and lista_posicoes[linhas][1] and lista_posicoes[linhas][2] == jogador2:
            print("Jogador 2, VENCEU")
            venceu = True
            return venceu
    for linhas in range(0, 3):
        if lista_posicoes[0][linhas] and lista_posicoes[1][linhas] and lista_posicoes[2][linhas] == jogador1:
            print("Jogador 1, VENCEU")
            venceu = True
            return venceu
        if lista_posicoes[0][linhas] and lista_posicoes[1][linhas] and lista_posicoes[2][linhas] == jogador2:
            print("Jogador 2, VENCEU")
            venceu = True
            return venceu


if __name__ == "__main__":
    lista_posicoes = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    menu_principal()
    jogador2 = ""
    jogador1 = int(input("Jogador 1, Digite o que será nesse jogo: "))
    jogador1, jogador2 = menu_escolha(jogador1, jogador2)
    desenho_forca(lista_posicoes)
    venceu = False
    while True:
        jogada1 = int(input("Jogador 1, digite a posição deseja jogar:  "))
        jogada2 = ""
        jogada(jogada1, jogada2)
        jogada2 = int(input("Jogador 2, digite a posição deseja jogar:  "))
        jogada(jogada1, jogada2)

        if venceu == True:
            print("FIM DE JOGO")
            break