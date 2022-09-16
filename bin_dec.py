dividendo = int(input("Digite um numero (Base decimal) para ser convertido em Binário: "))
numero_digitado = dividendo
quociente = 1
lista = []

while quociente >= 1:
    resto = dividendo%2
    lista.insert(0, resto)
    quociente = dividendo // 2
    dividendo = quociente

binario = ''.join([str(item) for item in lista])
print("O número",numero_digitado,", quando convertido em binário, vale:",binario)