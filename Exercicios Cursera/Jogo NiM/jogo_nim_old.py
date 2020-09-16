def fatorial_continuo():
    val = "1"
    while val != "sair":
        val=input('Digite um número para que seja exibido o fatorial, ou digite "sair" para encerrar.')
        if val.isdigit():
            fatorial(int(val))
        else:
            print('Favor digitar um número, ou digite "sair" para que o sistema seja encerrado.')
    print('Obrigado pela preferencia, até mais.')

def fatorial(num):
    i = 1
    resultado = 1
    while i <= num:
        resultado =resultado * i
        i += 1
    print(f'O fatorial de {num} é {resultado}')
                
fatorial_continuo()