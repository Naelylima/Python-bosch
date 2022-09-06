def contador():
    while True:
        numero = input("Fatorial de: ")
        count = numero
        try:
            count = int(numero)
            break
        except:
            print("VOCE NAO DIGITOU UM NUMERO")

    result = 1
    while (count > 1):
        result = result * count
        count -= 1
        print(result)

if __name__=='__main__':
  contador()

