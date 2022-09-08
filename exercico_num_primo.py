def num_primo():
    lista = []
    num = int(input("Digite o valor para verificar se ele é primo: "))

    for c in range(1, num + 1):
        if num % c == 0:
            lista.append(c)
    if len(lista) ==2:
        print("O NUMERO É PRIMO")
    else:
        print(lista)
        print("NÃO É PRIMO")

if __name__ == '__main__':
 num_primo()


