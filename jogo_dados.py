import random
import time


class Jogo:
    def __init__(self, nome, creditos, revanche1=False, parar = False):
        self.nome = nome
        self.creditos = creditos
        self.revanche1 = revanche1
        self.parar = parar


def inicio():
    lista = [1, 2, 3, 4, 5, 6]
    print("\n-------------------- O JOGO VAI COMEÇAR --------------------")
    print(f"Bem vindo(a) {jogador.nome}!\nVocê inicia a partida com R${jogador.creditos} de créditos.")
    num_jogador = int(input(f"{jogador.nome}, digite o valor do dado (1-6): "))
    while True:
        if jogador.parar == True:
            print(f'Tchazinho {jogador.nome}')
            break
        if num_jogador > 6 or num_jogador < 1:
            num_jogador = int(input("Digite um valor de 1-6: "))
        else:
                print("O computador está escolhendo um número ...")
                time.sleep(1)

        if lista.__contains__(num_jogador):
            if jogador.revanche1 == False:
                while True:
                    if jogador.creditos < 2:
                        print(f'Seu saldo é insuficiente: R${jogador.creditos}')
                        saldo_adc= int(input('Adicione mais saldo para continuar: R$'))
                        jogador.creditos+= saldo_adc

                    else:
                        jogador.creditos -= 2
                        lista.remove(num_jogador)
                        num_comp = random.choice(lista)
                        print(
                            f'\n{jogador.nome}, seu número é: {num_jogador} e número escolhido pelo computador é: {num_comp}.')
                        time.sleep(1)
                        jogar_dados(num_jogador, num_comp)
                        break

            else:
                lista.remove(num_jogador)
                num_comp = random.choice(lista)
                print(f'\n{jogador.nome}, seu número é: {num_jogador} e número escolhido pelo computador é: {num_comp}.')
                time.sleep(1)
                jogar_dados(num_jogador, num_comp)
                break


def jogar_dados(num_jogador, num_comp):
    print("\n ---------- OS DADOS FORAM LANÇADOS ---------- ")
    time.sleep(1)
    print("             *    SORTEANDO    *                 ")
    time.sleep(2)
    num_dados = random.randint(1,6)
    print(f'************ O numero do dado é: {num_dados} *************')
    print('-' * 48)
    verificar(num_dados, num_jogador, num_comp)


def verificar(num_dados, num_jogador, num_comp):
    if num_dados == num_jogador:
        if jogador.revanche1 ==True:
            print(f'{jogador.nome}, VOCÊ VENCEU !!!')
            jogador.creditos += 8
            print(f'Você ganhou R$8,00 de Crédito. Seu crédito atual é de: {jogador.creditos}')
            menu()
        if jogador.revanche1 == False:
            print(f'{jogador.nome}, VOCÊ VENCEU !!!')
            jogador.creditos += 4
            print(f'Você ganhou R$ 4,00 de Crédito. Seu crédito atual é de: {jogador.creditos}')
            revanche()

    elif num_dados == num_comp:
        print('O Computador venceu essa partida !! ')
        menu()

    else:
        print('Ninguém ganhou essa rodada, os dados serão jogados novamente')
        time.sleep(3)
        jogar_dados(num_jogador, num_comp)


def revanche():
    print('\nO computador sugeriu uma revanche! O dobro ou nada')
    print('Se você vencer você ganha mais R$ 4,00 de créditos para jogar')
    resposta = int(input('\n[1] Sim'
                         '\n[2] Não'
                         '\nDigite o número referente a sua resposta:'))
    if resposta == 1:
        jogador.creditos -= 4
        jogar_dados_revanche()
        jogador.revanche1 = True
    else:
        menu()


def jogar_dados_revanche():
    jogador.revanche1 = True
    lista = [1, 2, 3, 4, 5, 6]
    print('\n************** A REVANCHE VAI COMEÇAR *************')
    num_jogador = int(input(f"{jogador.nome}, digite o valor do dado (1-6): "))
    while True:
        if num_jogador > 6 or num_jogador < 1:
            num_jogador = int(input("Digite um valor de 1-6: "))
        else:
            print("O computador está escolhendo um número ...")
            time.sleep(1)
        if lista.__contains__(num_jogador):
            jogador.creditos -= 2
            lista.remove(num_jogador)
            num_comp = random.choice(lista)
            print(f'\n{jogador.nome}, seu número é: {num_jogador} e número escolhido pelo computador é: {num_comp}.')
            time.sleep(1)
            jogar_dados(num_jogador, num_comp)
            break
    jogador.revanche1 = True



def menu():
        print('\n---------------- MENU ----------------'
              '\n[1]- Jogar novamente'
              '\n[2]- Encerrar')
        resposta = int(input('Digite a opção desejada: '))
        if resposta == 1:
            inicio()
        else:
            jogador.parar=True




if __name__ == '__main__':
    jogador = Jogo(input("Digite seu nome: ").title(),
                   int(input("Cada partida são R$2,00.\nDigite o valor de crédito que deseja jogar: ")))
    while True:
        if jogador.creditos % 2 != 0:
            jogador.creditos = int(input('Digte um válor de numero par, por favor: '))
        else:
            inicio()
            break
