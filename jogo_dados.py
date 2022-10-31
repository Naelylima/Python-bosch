import random
import time


class Jogo :
    def __init__(self, nome, creditos ):
        self.nome = nome
        self.creditos = creditos


def inicio():
    lista = [1, 2, 3, 4,5 ,6]
    print("\n-------------------- O JOGO VAI COMEÇAR --------------------")
    print(f"Bem vindo(a) {jogador.nome}!\nVocê inicia a partida com R${jogador.creditos} de créditos.")
    num_jogador = int(input(f"{jogador.nome}, digite o valor do dado (1-6): "))
    while True:
        if num_jogador >6 or num_jogador <1:
            num_jogador= int(input("Digite um valor de 1-6: "))
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

def jogar_dados(num_jogador, num_comp):
    print("\n ---------- OS DADOS FORAM LANÇADOS ---------- ")
    time.sleep(1)
    print("             *    SORTEANDO    *                 ")
    time.sleep(2)
    num_dados = random.randint(1, 6)
    print(f'************ O numero do dado é: {num_dados} *************')
    print('-' * 48)
    verificar(num_dados, num_jogador, num_comp)

def verificar(num_dados, num_jogador, num_comp):
    if num_dados == num_jogador:
        print(f'{jogador.nome}, VOCÊ VENCEU !!!')
        jogador.creditos += 4
        print(f'Você ganhou R$ 4,00 de Crédito. Seu crédito atual é de: {jogador.creditos}')
        # vencer = False
        # revanche(vencer)
        menu()

    elif num_dados == num_comp:
        print('O Computador venceu essa partida !! ')
        menu()
    else:
        print('Ninguém ganhou essa rodada, os dados serão jogados novamente')
        time.sleep(3)
        jogar_dados(num_jogador, num_comp)

def revanche(vencer):
    vencer = False
    print('\nO computador sugeriu uma revanche! O dobro ou nada')
    print('Se você vencer você ganha mais R$ 4,00 de créditos para jogar')
    resposta = int(input('\n[1] Sim'
                         '\n[2] Não'
                         '\nDigite o número referente a sua resposta:'))
    if resposta == 1:
        print('************** A REVANCHE VAI COMEÇAR *************')
        inicio()
        if vencer == True:
            jogador.creditos += 4
            print('Você ganhou mais 4 reais de credito')

    else:
        menu()

def menu():
    print('MENU')




if __name__ == '__main__':
    jogador = Jogo(input("Digite seu nome: ").title(), int(input("Cada partida são R$2,00.\nDigite o valor de crédito que deseja jogar: ")))
    while True:
        if jogador.creditos %2 != 0 :
            jogador.creditos = int(input('Digte um válor de numero par, por favor: '))
        else:
            inicio()
            break






