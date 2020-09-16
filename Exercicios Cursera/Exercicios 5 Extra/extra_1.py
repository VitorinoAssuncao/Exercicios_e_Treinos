
def primo(n):
    i = 1
    multiplicadores = []
    while i <= n:
        if n % i == 0:
            multiplicadores.append(i)
        i += 1
    if len(multiplicadores) == 2:
        return n
    else:
        return 0

def n_primos(num):
    i = 2
    primos = []
    while i <= num:
        if primo(i) != 0:
            primos.append(i)
        i += 1
    return len(primos)

i = int(input("Digite o valor a ser verificado: "))
print(n_primos(i))