def conta_letras(frase,parametro = 'vogais'):
    vogais = 0
    consoante = 0
    for i in frase:
        if verifica_vogal(i) == True:
            vogais += 1
        else:
            consoante += 1
    
    if parametro == 'vogais':
        return vogais
    elif parametro == 'consoantes':
        return consoante 
    else:
        return vogais

def verifica_vogal(letra):
    if letra in ['A','E','I','O','U','a','e','i','o','u']:
        return True
    else:
        return False