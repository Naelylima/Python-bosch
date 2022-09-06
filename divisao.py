def divisao():
    a = int(input("Entre com o valor do dovisor: "))
    b = int(input('Digite o valor do dividendo: '))
    result = a/b
    print("O resultado é: ",result)
    print("O tipo de resultado é: ", type(result))
    result_int = a//b
    print("O resultado é: ", result_int)
    print("O tipo de resultado é: ", type(result_int))
    result_r = a % b
    print("O resultado é: ", result_r)
    print("O tipo de resultado é: ", type(result_r))


if __name__ == '__main__':
    divisao()
