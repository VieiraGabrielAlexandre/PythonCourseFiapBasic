episodios = 24

def cadastrarAnime(lista):
    resposta = 'S'

    while resposta == 'S':
        animes = [input('Nome: '),
                  int(input('Temporadas: ')),
                  input('Estudio: ')]
        lista.append(animes)

        resposta = input('Deseja continua (s): ').upper()

def exibirAnimes(lista):
    for elemento in lista:
        print('Nome............:', elemento[0])
        print('Temporadas......:', elemento[1])
        print('Episodios.......:', elemento[1] * episodios)
        print('Estudio.........:', elemento[2])

def localizarAnime(lista):
    busca = input('Digite o nome do anime: ')
    for elemento in lista:
        if busca == elemento[0]:
            print('Temporadas..:', elemento[1])
            print('Episodios...:', elemento[1] * 24)
            print('Estudio.....:', elemento[2])

def excluirAnime(lista):
    exclui = input('Digite o nome do anime: ')
    for elemento in lista:
        if exclui == elemento[0]:
            lista.remove(elemento)

    return "Anime excluido"

def finalizarLista(lista):
    for elemento in lista:
        print("Anime : ", elemento[0])
        print("Temporadas : ", elemento[1])
        print("Episodios : ", elemento[1] * episodios)
        print("Estudio: ", elemento[2])
