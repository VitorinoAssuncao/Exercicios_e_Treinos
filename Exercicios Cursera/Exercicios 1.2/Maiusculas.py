def maiusculas(frase):
    resultado = ''
    for i in frase:
        if ord(i) >= 65 and ord(i) <= 92:
            resultado += i

    return resultado