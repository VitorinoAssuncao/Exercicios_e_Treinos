# def reverse_print(lista):
#     for i in range(len(lista)-1,-1,-1):
#         print(lista[i])

# number = 1
# list_numbers = []
# while number != 0:
#     number = int(input('Digite um número: '))
#     if number != 0:
#         list_numbers.append(number)
#     else:
#         reverse_print(list_numbers)

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]

print(lista1 is lista2)
print(lista1 is lista3)
print(lista2 is lista3)
print(lista3 is lista2)
print(lista1 == lista2)
print(lista3 == lista1)




