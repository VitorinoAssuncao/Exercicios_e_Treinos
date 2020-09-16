numero = int(input('Digite o número a ser verificado:'))
if (numero % 5 == 0) and (numero % 3 == 0):
    print('FizzBuzz')
else:
    print(numero)