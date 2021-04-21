lista = []
episodios = 24
resposta = 'S'

while resposta == 'S':
    animes = [input('Nome: '),
             int(input('Temporadas: ')),
             input('Estudio: ')]
    lista.append(animes)

    resposta = input('Deseja continua (s): ').upper()

for elemento in lista:
    print('Anime: ', elemento[0])

busca = input('\nDigite o nome do anime: ')

for indice in lista:
    if busca == indice[0]:
        print('Anime: ', indice[0])
        print('Temporadas: ', indice[1])
        print('Estudios: ', indice[2])

temporada = input('\nDigite o nome do anime para cadastrar episodios: ')

for elemento in lista:
    if temporada == elemento[0]:
        print('Temporadas antigas: ', elemento[1])
        elemento[1] = elemento[1] + 1
        print('Temporadas atualizadas: ', elemento[1])
        print('Tempo de episodios: ', elemento[1] * episodios)

excluir = input('\nDigite o nome do anime a ser excluido: ')

for elemento in lista:
    if elemento[0] == excluir:
        lista.remove(elemento)

for elemento in lista:
    print('Nome...........:', elemento[0])
    print('Temporadas.....:', elemento[1])
    print('Estudio........:', elemento[2])

temporadas = []
for elemento in lista:
    temporadas.append(elemento[1])
if len(temporadas) > 0:
    print('O anime com mais episodios tem ', max(temporadas), 'temporadas')
    print('O anime com menos episodios tem ', min(temporadas), 'temporadas')
    print('O total de episodios de animes episodios', sum(temporadas) * episodios)