def imprime_quadrado(alt,larg):
    i = 1
    texto = ""
    while i <= alt:
        x = 1
        while x <= larg:
            texto += "#"
            x += 1
        print(texto) 
        texto = ""
        i += 1


larg=int(input("Digite a largura: "))
alt=int(input("Digite a altura:"))

imprime_quadrado(alt,larg)
            
