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
                print("-" * 38)
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
                print("-" * 38)
                return jogador_1, jogador_2
        except ValueError:
            print("Você digitou algo errado\n")
            continue

def verificar(par):
    for i in range(3):
        for j in range(3):
            if par == lista_posicoes[i][j]:
                return i, j
    return None, None

def jogadas(jogada1, jogador):
    vencer = False
    linha, coluna = verificar(jogada1)
    if linha != None:
        if jogador == 1:
            lista_posicoes[linha][coluna] = jogador1
        else:
            lista_posicoes[linha][coluna] = jogador2
        vencer = vitoria(vencer=venceu)
    else:
        print("Essa opção já foi escolhida")
        seguir_jogo = False
        return seguir_jogo

    desenho_forca(lista_posicoes)
    return vencer

def vitoria(vencer):
    vencer = False
    for linhas in range(0, 3):
        if lista_posicoes[linhas][0] == jogador1 and lista_posicoes[linhas][1] == jogador1 and lista_posicoes[linhas][2] == jogador1:
            print("*" * 30)
            print("Jogador 1, VENCEU")
            print("*" * 30)
            vencer = True
            return vencer
        if lista_posicoes[linhas][0] == jogador2 and lista_posicoes[linhas][1] == jogador2 and lista_posicoes[linhas][2] == jogador2:
            print("*" * 30)
            print("Jogador 2, VENCEU")
            print("*" * 30)
            vencer = True
            return vencer
    for linhas in range(0, 3):
        if lista_posicoes[0][linhas] == jogador1 and lista_posicoes[1][linhas] == jogador1 and lista_posicoes[2][linhas] == jogador1:
            print("*" * 30)
            print("Jogador 1, VENCEU")
            print("*" * 30)
            vencer = True
            return vencer
        if lista_posicoes[0][linhas] == jogador2 and lista_posicoes[1][linhas] == jogador2 and lista_posicoes[2][linhas] == jogador2:
            print("*" * 30)
            print("Jogador 2, VENCEU")
            print("*" * 30)
            vencer = True
            return vencer
    if lista_posicoes[0][0] == jogador1 and lista_posicoes[1][1] == jogador1 and lista_posicoes[2][2] == jogador1:
        print("*"*30)
        print("Jogador 1, VENCEU")
        print("*" * 30)
        vencer = True
        return vencer
    elif lista_posicoes[0][0] == jogador2 and lista_posicoes[1][1] == jogador2 and lista_posicoes[2][2]== jogador2:
        print("*" * 30)
        print("Jogador 2, VENCEU")
        print("*" * 30)
        vencer = True
        return vencer

    return vencer

if __name__ == "__main__":
    lista_posicoes = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    menu_principal()
    seguir_jogo = True
    venceu = False
    jogador2 = ""
    jogador1 = int(input("Jogador 1, Digite o que será nesse jogo: "))
    jogador1, jogador2 = menu_escolha(jogador1, jogador2)
    desenho_forca(lista_posicoes)
    while True:
        venceu = vitoria(venceu)
        while True:
            if venceu == True:
                break
            else:
                jogada1 = int(input("Jogador 1, digite a posição deseja jogar:  "))
                venceu = jogadas(jogada1, 1)
                if venceu == True:
                    break
                venceu = jogada2 = int(input("Jogador 2, digite a posição deseja jogar:  "))
                jogadas(jogada2, 2)
                if venceu == True:
                    break
        break


