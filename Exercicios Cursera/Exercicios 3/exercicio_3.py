n = input('Digite o número inteiro:')
i = 0
resultado = 0
while i < len(n):
    resultado += int(n[i]) 
    i += 1
print(resultado)