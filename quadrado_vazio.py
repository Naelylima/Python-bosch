def quadrado_vazio():
    n = int(input("Digite um número: "))
    print(' *' * n)
    for i in range (1, n -1):
        print(' *' + '  '*(n-2) + ' *')
    print(' *'*n)

if __name__ == '__main__':
        quadrado_vazio()
