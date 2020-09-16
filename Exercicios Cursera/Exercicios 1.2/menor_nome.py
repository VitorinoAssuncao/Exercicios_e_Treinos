def menor_nome(nomes):
    resultado = []
    nome_final = ""
    nomes_processados = processa_nomes(nomes)
    for i in range(0,len(nomes_processados)):
        if (i == 0):
            resultado.append(nomes_processados[i])
        else:
            if len(nomes_processados[i]) < len(resultado[0]):
                resultado[0] = nomes_processados[i]
    nome_final = retorna_maiuscula(resultado[0])
    return nome_final

def remove_espacos(nome):
    resultado = ""
    for i in range(0,len(nome)):
        if ord(nome[i]) != 32:
            resultado += nome[i]
    return resultado

def processa_nomes(nomes):
    nomes_processados = []
    for i in nomes:
        nomes_processados.append(remove_espacos(i))
    return nomes_processados

def retorna_maiuscula(nome):
    nome_finalizado = ""
    if ord(nome[0]) >= 97 and ord(nome[0]) <= 122:
        nome_finalizado += chr(ord(nome[0]) - 32)
    nome_finalizado += nome[1:]
    return nome_finalizado   

