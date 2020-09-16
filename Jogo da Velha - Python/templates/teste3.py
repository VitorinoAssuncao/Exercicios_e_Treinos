a=(int(input("Digite o 1° número: ")))
b=(int(input("Digite o 2°número: ")))
c=(str(input("Digite o tipo de operação +,-,*,/ ")))

if (c == '+'):
    soma= a + b
    print(soma)
elif (c == '-'):
    sub = a -b
    print(sub)
elif(c == '*'):
    mult= a * b
    print(mult)
elif( c == '/'):
    divisao= a / b
    print( divisao)   
else :
    print("Não entendi sua escolha, digite novamente")          