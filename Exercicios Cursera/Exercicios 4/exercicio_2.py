def primo(numero):
    i = 1
    multiplicadores = []
    while i <= numero:
        if numero % i == 0:
            multiplicadores.append(i)
        i += 1
    if len(multiplicadores) == 2:
        return True
    else:
        return False

def maior_primo(numero):
    while primo(numero) == False:
        numero -= 1
    return numero
