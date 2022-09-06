def fatorial_for():
    while True:
        numero = input("Fatorial de: ")
        count = numero
        try:
            count = int(numero)
            break
        except:
            print("VOCE NAO DIGITOU UM NUMERO")

    result = 1
    for count in range(count,1, -1):
        result = result * count
        print(result)

if __name__=='__main__':
  fatorial_for()

