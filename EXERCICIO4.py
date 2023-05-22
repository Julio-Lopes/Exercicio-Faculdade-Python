def cadastrarProduto(lista,acomulador):  #FUNÇÃO CRIADA PARA CADASTRAR PRODUTO
    cadastro = {}  #VARIAVEL PARA RECEBER OS DADOS DOS PRODUTOS
    
    while True:
        cadastro.clear  #FUNÇÃO PARA DELETAR OS DADOS CONTIDOS NA VARIAVEL CADASTRO
        print('Voce selecionou a opção de Cadastrar Produto')  
        contador = acomulador  #TOTAL DE CADASTROS EFETUADOS
        print('Codigo do produto {:0>3}'.format(contador))  #SAIDA COM O CODIGO DO PRODUTO QUE VAI SER CADASTRADO
        cadastro['codigo'] = contador  #VARIAVEL PARA RECEBER O CODIGO DO PRODUTO
        cadastro['nome'] = str(input('Por favor entre com o NOME do produto: ')) #VARIAVEL PARA RECEBER O NOME DO PRODUTO
        cadastro['fabricante'] = str(input('Por favor entre com o FABRICANTE do produto: '))  #VARIAVEL PARA RECEBER O FABRICANTE DO PRODUTO
        cadastro['valor'] = float(input('Por favor entre com o VALOR(R$) do produto: '))  #VARIAVEL PARA RECEBER O VALOR DO PRODUTO
        return cadastro

def consultarProduto(lista):  #FUNÇAO CRIADA PARA CONSULTAR PRODUTOS JA CADASTRADOS
    while True:
        print('Voce selecionou a opção de Consultar Produto')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos os Produtos')                             #MENU PARA O USUARIO SELECIONA UMA DAS OPÇÕES
        print('2 - Consultar Produtos por Codigo')
        print('3 - Consultar Produtos por Fabricante')
        print('4 - Retornar')

        try:
            opcao = int(input()) #ENTRADA PARA O USUARIO SELECIONA UMA DAS OPÇÕES

            if opcao == 1:  #FUNÇÃO PARA CONSULTAR TODOS OS PRODUTOS
                for i in lista:
                    print('Codigo : {}'.format(i['codigo']))
                    print('Nome : {}'.format(i['nome']))
                    print('Fabricante : {}'.format(i['fabricante']))       #SAIDA COM AS INFORMAÇÕES DO PRODUTO PESQUISADO
                    print('Valor : {}'.format(i['valor']))

            elif opcao == 2:  #FUNÇÃO PARA CONSULTAR UM PRODUTO ESPECIFADO PELO CODIGO DO PRODUTO
                cod = int(input('Digite o CODIGO do produto: '))
                for i in lista:
                    if i['codigo'] == cod:
                        print('Codigo : {}'.format(i['codigo']))
                        print('Nome : {}'.format(i['nome']))                  #SAIDA COM AS INFORMAÇÕES DO PRODUTO PESQUISADO
                        print('Fabricante : {}'.format(i['fabricante']))
                        print('Valor : {}'.format(i['valor']))

            elif opcao == 3:  #FUNÇÃO PARA CONSULTAR UM PRODUTO ESPECIFADO PELO NOME DO FABRICANTE
                fabricante = str(input('Digite o FABRICANTE do(s) produto(s): '))
                for i in lista:
                    if i['fabricante'] == fabricante:
                        print('Codigo : {}'.format(i['codigo']))
                        print('Nome : {}'.format(i['nome']))
                        print('Fabricante : {}'.format(i['fabricante']))        #SAIDA COM AS INFORMAÇÕES DO PRODUTO PESQUISADO
                        print('Valor : {}'.format(i['valor']))

            elif opcao == 4:  #FUNÇÃO PARA RETORNAR AO MENU PRINCIPAL
                break

            else:  #FUNÇÃO PARA CASO O USUARIO SELECIONE UMA OPÇÃO NÃO EXISTENTE NO MENU
                print('opção invalida, entre com uma das opções do menu')  #SAIDA PARA CASO O USUARIO SELECIONE UMA OPÇÃO NÃO EXISTENTE NO MENU
                continue

        except ValueError:  #FUNÇÃO CASO O USUARIO DIGITE UM VALOR NÃO NUMERICO
            print('opção invalida, entre com uma das opções do menu') #SAIDA CASO O USUARIO DIGITE UM VALOR NÃO NUMERICO
            continue

def removerProduto(lista):  #FUNÇÃO CRIADA PARA EXCLUIR UM PRODUTO
    while True:
        print('Voce selecionou a Opção de remover Produto') #SAIDA COM A OPÇÃO EXECUTADA PELO USUARIO

        try:
            remover = int(input('Digite o codigo do produto a ser removido: '))  #ENTRADA PARA O USUARIO ESPEFICFICAR O PRODUTO A SER EXCLUIDO
    
            for i in lista: #FUNÇÃO PARA BUSCAR O PRODUTO A SER EXCLUIDO
                if i['codigo'] == remover:
                    del lista[remover - 1]  #FUNÇÃO PARA EXCLUIR O PRODUTO
                    return lista
                    
        except ValueError:  #FUNÇAO PARA CASO DO USUARIO NÃO DIGITAR UM VALOR NUMERICO
            print('opção invalida, entre com um codigo de produto valido') #SAIDA PARA CASO DO USUARIO NÃO DIGITAR UM VALOR NUMERICO

#PROGRAMA PRINCIPAL
lista = []  #VARIAVEL PARA FAZER A LISTA DE CADASTRO
acomulador = 0 #VARIAVEL PARA CRIAR O NUMERO TOTAL DE CADASTRO
while True:
    print('Bem Vindo ao Controle de Estoque da Mercearia do Julio Cesar Ribeiro Lopes')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Produto')                                                          #MENU DE OPÇÕES PARA O USUARIO ESCOLHER      
    print('2 - Consultar Produto(s)')
    print('3 - Remover Produto')
    print('4 - Sair')

    try:
        opcao = int(input(''))  #ENTRADA PARA O USUARIO ESCOLHER UM DAS OPÇÕES DO MENU

        if opcao == 1: #FUNÇÃO PARA DEFINIR ESCOLHA DO USUARIO
            acomulador = acomulador + 1
            lista.append(cadastrarProduto(lista,acomulador)) #FUNÇÃO PARA CRIAR UM PRODUTO
            continue

        elif opcao == 2: #FUNÇÃO PARA DEFINIR ESCOLHA DO USUARIO
            consultarProduto(lista) #FUNÇÃO PARA CONSULTADO UM PRODUTO
            continue

        elif opcao == 3: #FUNÇÃO PARA DEFINIR ESCOLHA DO USUARIO
            removerProduto(lista)
            continue

        elif opcao == 4: #FUNÇÃO PARA DEFINIR ESCOLHA DO USUARIO
            break  #SAIR DO PROGRAMA

        else: #FUNÇÃO PARA CASO DE O USUARIO NÃO ESCOLHER UMA OPÇÃO VALIDA
            print('opção invalida, entre com uma das opções do menu')  #SAIDA PARA CASO DE O USUARIO NÃO ESCOLHER UMA OPÇÃO VALIDA
            continue

    except ValueError:  #FUNÇÃO PARA O CASO DE O USUARIO NÃO DIGITAR UM VALOR NUMERICO
        print('opção invalida, entre com uma das opções do menu') #SAIDA PARA O CASO DE O USUARIO NÃO DIGITAR UM VALOR NUMERICO
        continue