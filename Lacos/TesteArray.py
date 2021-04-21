equipamentos = []
valores = []
serials = []
resposta = 'S'

while resposta == 'S':
   equipamentos.append(input('Equipamento: '))
   valores.append(float(input('Valores: ')))
   serials.append(int(input('Serials: ')))
   resposta = input('Deseja continuar')

for indice in range(0, len(equipamentos)):
    print('\nEquipamento ..:', (indice + 1))
    print('Nome............:', equipamentos[indice])
    print('Valor...........:', valores[indice])
    print('Serial..........:', equipamentos[indice])