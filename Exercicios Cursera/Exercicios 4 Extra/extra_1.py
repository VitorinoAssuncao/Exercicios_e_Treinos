def fizzbuzz(numero):
    resposta = ''
    if (numero % 3 == 0) and (numero % 5 != 0):
        resposta = 'Fizz'
    elif (numero % 3 != 0) and (numero % 5 == 0):
        resposta = 'Buzz'
    elif (numero % 3 == 0) and (numero % 5 == 0):
        resposta = 'FizzBuzz'
    else:
        return numero

    return resposta