def pascal():
    base_final = int(input("Digite o valor da base, (maior que dois): "))
    lista_atual = []
    lista_aux = []

    for base_atual in range(0, base_final):
        for pos in range(0, base_atual+1):
            if pos == 0 or pos == base_atual:
                lista_atual.append(1)
            else:
                lista_atual.append(lista_aux[pos] + lista_aux[pos-1])
        lista_aux = lista_atual[:]
        lista_atual.clear()
        print(lista_aux)

if __name__ == "__main__":
    pascal()

