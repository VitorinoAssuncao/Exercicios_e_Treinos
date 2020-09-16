n=int(input('Digite um número inteiro:'))
i = 1
multiplicadores = []
while i <= n:
    if n % i == 0:
        multiplicadores.append(i)
    i += 1
if len(multiplicadores) == 2:
    print('primo')
else:
    print('não primo')