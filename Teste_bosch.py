def contador ():
    numero = int(input("Fatorial de : "))
    count = numero

    while count> 1:
        numero =  numero*(count-1)
        count -=1
        print(numero)


if __name__  == ' __main__ ':
    contador()