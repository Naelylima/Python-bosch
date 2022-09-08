def triagulo():
    aux = ''
    cont = 0
    n = int(input("Digite um número: "))

    for linha in range(n):
        aux = aux + '* '
        cont += 1
        print(aux)

if __name__ == '__main__':
        triagulo()
