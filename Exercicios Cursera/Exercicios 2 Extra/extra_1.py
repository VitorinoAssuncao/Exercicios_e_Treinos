import math

x_1 = int(input('Digite a coordenada X, da primeira posição:'))
y_1 = int(input('Digite a coordenada Y, da primeira posição:'))
x_2 = int(input('Digite a coordenada X, da segunda posição:'))
y_2 = int(input('Digite a coordenada Y, da segunda posição:'))

resultado = math.sqrt((x_1+y_1)**2+(x_2+y_2)**2)
if resultado >= 10:
    print('longe')
else:
    print('perto')