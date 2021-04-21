animes = []
episodios = []
estudio = []
resposta = 'S'

while resposta == 'S':
    animes.append(input('Nome: '))
    episodios.append(int(input('Episodios: ')))
    estudio.append(input('Estudio: '))
    resposta = input('Deseja continua (s): ').upper()

busca = input('Anime: ')

for indice in range(0, len(animes)):
    if busca == animes[indice]:
        print('Anime: ', animes[indice])
        print('Episodios: ', episodios[indice])
        print('Estudios: ', estudio[indice])
