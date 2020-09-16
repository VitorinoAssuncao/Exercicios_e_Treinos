def imprime_quadrado(alt,larg):
    i = 1
    texto = ""
    while i <= alt:
        x = 1
        while x <= larg:
            if (i == 1 or i == alt):
                texto += "#"
            else:
                if (x == 1 or x == larg):
                    texto += "#"
                else:
                    texto += " "
            x += 1
        print(texto) 
        texto = ""
        i += 1


larg=int(input("Digite a largura: "))
alt=int(input("Digite a altura:"))

imprime_quadrado(alt,larg)
            
