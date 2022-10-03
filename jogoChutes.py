import random
import time

def escolha():
    while True:
        pergunta = input('Deseja jogar novamente? Se sim aperte enter e senão aperte qualquer tecla.\n')
        if pergunta == '':
            jogo()
        else:
            break


def jogo ():
    vida = 50
    aleatorio = random.randint(1, 100)
    chutes = 0
    while (chutes < 3):
            try:
                chute = int(input(f"Digite um número entre 1 e 100: "))
                diferenca = aleatorio - chute
                if chute > 100 or chute < 1:
                    print("Chute um número dentro do limite maximo e minimo\n")
                    continue
                if diferenca < 0 :
                    diferenca = diferenca * -1
                    vida -= diferenca
                else:
                    vida -= diferenca
                if chute == aleatorio:
                    print(f"Você acertou!, o número era {aleatorio}")
                    break


                elif vida <= 0 :
                    print(f"Você estorou suas vidas, o número era {aleatorio}")
                    break

                elif chute > aleatorio:
                    print(
                        f'Você errou, Chutou alto demais, o número é menor que {chute}.\nSua vida está em {vida} pontos\n')
                elif chute < aleatorio:
                    print(f'Você errou, Chutou baixo demais, o número é maior que {chute}.\nSua vida está em {vida} pontos\n')
                chutes = chutes + 1
                if chutes == 3 :
                    print('***** Você estou suas chanches *****')
            except ValueError:
                print("Você digitou algo errado, tente novamente\n")
                continue




if __name__ == "__main__":
    print("******************************** O JOGO VAI COMEÇAR! ************************************")
    time.sleep(1.0)
    print("Você tera 50 pontos de vida e terá três chanches para acertar o número que estou pensando ")
    print("-" * 90)
    time.sleep(1.0)
    jogo()
    escolha()
