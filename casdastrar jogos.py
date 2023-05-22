def exar (na):
    try:
        a = open (na, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True 

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except: 
        print('erro na criaçao do arquivo')

    else:
        print('arquivo {} foi criado com sucesso'.format(nomeArquivo))

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideo):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('erro ao abrir o arquivo')
    else:
        a.write('{} ; {} \n'.format(nomeJogo,nomeVideo))
    finally:
        a.close()

def listaAquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('erro ao abrir a lista de jogo')
    else:
        print(a.read())
    finally:
        a.close()


arquivo = 'games.txt'

if exar (arquivo):
    print('arquivo localizado no computador')
else:
    print('arquivo nao existe')
    criaArquivo(arquivo)

while True:
    print('menu')
    print('1 - cadastrar novo jogo')
    print('2 - lista de jogos')
    print('3 - sair')

    x = int(input('escolha a opção desejada: '))

    if x == 1:
        print('cadastro de jogos')
        nomeJogo = input('coloque o nome do jogo: ')
        nomeVideo = input('coloque o nome do video game: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideo)

    elif x == 2:
        print('lista de jogos')
        listaAquivo(arquivo)
    
    elif x == 3:
        print('encerrando programa')
        break