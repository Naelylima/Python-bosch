import random
from bonecos import*

def comeco():
    print("-"*31)
    print("\nSEJA BEM-VINDO AO JOGO DA FORCA!\n")
    print("-" * 31)

def jogo_forca():
    chances = 6
    palavras_lista = ["BOSCH", "ETS", "JOVEM", "SMART", "PYTHON"]
    dicas = ["Empresa", "Setor aprendiz", "Aprendiz", "Curso dentro da BOSCH", "Linguagem de programação"]
    palavra_aleatoria = random.choice(palavras_lista)
    palavra_certa = []
    for i in range(len(palavra_aleatoria)):
        palavra_certa.append(('-'))
    erros = []
    bonecos(chances)
    print('\nPalavra:', '-' * len(palavra_aleatoria))


    while True:
        for j in range(len(palavras_lista)):
            if palavra_aleatoria == palavras_lista[j]:
                print(f"\nA dica é: {dicas[j]}")
        letra = input("Digite uma letra: ").upper().replace(" ", "")


        if erros.__contains__(letra) or palavra_certa.__contains__(letra):
            letra = input("Você já digitou essa letra, digite outra diferente: ").replace(" ", "").upper()

        if letra.isdigit():
            print("Digite uma letra, não um número.")
            continue

        if len(letra) > 1:
            print("Digite apenas uma letra.")
            continue

        if palavra_aleatoria.__contains__(letra):
            for pos, encima in enumerate(palavra_aleatoria):
                if letra == encima:
                    palavra_certa.pop(pos)
                    palavra_certa.insert(pos, letra)
                    bonecos(chances)
                    print("Palavra: ", *palavra_certa)

            if "".join(palavra_certa) == palavra_aleatoria:
                print("Você ganhou! :)")
                escolha()
                break
        else:
            chances -= 1
            bonecos(chances)
            if chances < 1:
                print("Você perdeu :(")
                print(palavra_aleatoria)
                escolha()
                break
            erros.append(letra)
            print("Palavra: ", *palavra_certa)
            print(f"\nSeus erros são: {erros}")
            print(f"Você errou e tem {chances} chances\n")



def escolha():
    while True:
        decisao = input("Deseja continuar? Se sim dê enter, caso não digite 'SAIR': \n").upper().replace(" ", "")
        if decisao == "":
            print('-'*30)
            print('          NOVA RODADA')
            print('-' * 30)
            jogo_forca()
        if decisao == "SAIR":
            break
        else:
            continue

if __name__ == '__main__':
    comeco()
    jogo_forca()