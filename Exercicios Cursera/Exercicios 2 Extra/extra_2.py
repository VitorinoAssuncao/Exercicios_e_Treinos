import math

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

delta = (b**2) - (4 * a * c)

if delta > 0:
    raizes = 2
elif delta == 0:
    raizes = 1
else:
    raizes = 0


if raizes == 0:
    print('esta equação não possui raízes reais')
elif raizes == 1:
    x1 = ((-1 * b) + math.sqrt(delta))/ (2*a)
    print(f'a raiz desta equação é {x1}')
else:
    x1 = ((-1 * b) + math.sqrt(delta))/ (2*a)
    x2 = ((-1 * b) - math.sqrt(delta))/ (2*a)
    if x1 < x2:
        print(f'as raízes da equação são {x1} e {x2}')
    else:
        print(f'as raízes da equação são {x2} e {x1}')