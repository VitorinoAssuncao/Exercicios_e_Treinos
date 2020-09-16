numero = input('Digite um número inteiro:')
i = 0
total = 0
while i < (len(numero)-1):
    if numero[i] == numero[i+1]:
        total += 1
    i += 1

if total != 0:
    print('sim')
else:
    print('não')