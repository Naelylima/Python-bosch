import math

binario = int(input("Digite o número binario para ser convertido: "))
valor_digitado = binario
tamanho_binario = len(str(binario))
dec = 0
i = 0

while (tamanho_binario >= 0):
    resto = binario%10
    dec = dec + (resto*(2**i))
    tamanho_binario -= 1
    i += 1
    binario = binario//10
    print(dec)
print(i)

# print(valor_digitado)
# print(dec)