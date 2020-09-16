segundos_base=int(input('Digite a quantidade de segundos que deseja converter:'))

dias = segundos_base // 86400
horas = (segundos_base % 86400) // 3600
minutos = ((segundos_base % 86400) % 3600) // 60
segundos = ((segundos_base % 86400) % 3600) % 60 
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')


