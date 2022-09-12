def fatorial (n):
    print('RECEBI O PARAMENTRO ', n)
    result = 1
    if (n>=1):
        result = result *fatorial(n-1)
    return result


if __name__=='__main__':
    while True:
        numero = (input("Fatorial de: "))
        count = numero
        try:
            n = int(numero)
            break
        except:
            print("VOCE NAO DIGITOU UM NUMERO")

