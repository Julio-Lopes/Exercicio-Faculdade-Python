#FUNÇÕES CRIADAS
def volumeFeijoada(valor_volu):  #FUNÇÃO CRIADA PARA SABER O TAMANHO DA FEIJOADA O USUARIO IRA ESCOLHER
    print('Menu Volume Feijoada')  #SAIDA COM O MENU
    
    while True:
        try:
            volumeFeijoada = int(input('Entrei com a quantidade que voce deseja(ml): '))  #ENTRADA PARA QUE USUARIO ENTRE COM O TAMANHO DA FEIJOADA DESEJADA

            if volumeFeijoada < 300:  #FUNÇÃO PARA SABER O VALOR DA FEIJOADA ESCOLHIDA PELO USUARIO CASO SEJA UM VALOR TAMANHO VALIDO
                ('Não aceitamos porções menores que 300ml ou maiores 5l')   #SAIDA CASO O USUARIO NÃO DIGITE UM TAMANHO ACEITO PELA LOJA
                continue

            elif volumeFeijoada <= 5000:   #FUNÇÃO PARA SABER O VALOR DA FEIJOADA ESCOLHIDA PELO USUARIO CASO SEJA UM VALOR TAMANHO VALIDO                                                    
                valor_volu = volumeFeijoada * 0.08   #CALCULO PARA SABER O VALOR DA FEIJOADA 
                return valor_volu

            else:  #FUNÇÃO PARA SABER SE O USUARIO ESCOLHEU UM TAMANHO VALIDO
                print('Não aceitamos porções menores que 300ml ou maiores 5l')  #SAIDA CASO O USUARIO NÃO TENHA ESCOLHIDO UM VALOR VALIDO
                continue
            

        except ValueError:  #FUNÇÃO PARA CASO O USUARIO NÃO ENTRE COM UM VALOR NUMERICO
            print('Não aceitamos porções menores que 300ml ou maiores 5l')  #SAIDA CASO O USUARIO NÃO ENTRE COM UM VALOR NUMERICO
            continue
        
def opcaoFeijoada(valor_feijoada):  #FUNÇÃO CRIADA PARA SABER QUAL TIPO DE FEIJOADA O USUARIO IRA ESCOLHER
    print('Entre com a opção de Feijoada:')
    print('b - Básica (Feijão + paiol + costelinha')
    print('p - Premium (Feijão + paiol + costelinha + partes de porco')                                    #SAIDA COM O MENU PARA O USUARIO ESCOLHER O TIPO DE FEIJOADA DESEJADA
    print('s - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon')
    
    while True:
        opcaoFeijoada = input('').upper()  #ENTRADA PARA USUARIO SELECIONAR A FEIJOADA DESEJADA
        
        if opcaoFeijoada == 'B':
            valor_feijoada = 1   #VALOR PARA SABER O ACRESCIMO PARA CALCULA O VALOR FINAL DA FEIJOADA
            return valor_feijoada

        elif opcaoFeijoada == 'P':                                                                           #FUNÇÃO PARA SABER QUAL FEIJOADA O USUARIO ESCOLHEU
            valor_feijoada = 1.25   #VALOR PARA SABER O ACRESCIMO PARA CALCULA O VALOR FINAL DA FEIJOADA
            return valor_feijoada

        elif opcaoFeijoada == 'S':
            valor_feijoada = 1.50   #VALOR PARA SABER O ACRESCIMO PARA CALCULA O VALOR FINAL DA FEIJOADA
            return valor_feijoada
            

        else:
            print('Você não digitou uma opção válida')  #SAIDA CASO O USUARIO NÃO ESCOLHA UMA DAS OPÇÕES DESEJADA
            continue

def acompanhamentoFeijoada(valor_acom):  #FUNÇÃO CRIADA PARA CALCULAR OS ADICIONAIS DA FEIJOADA
    while True:
        print('Deseja mais algum acompanhamento:')
        print('0 - não desejo mais acompanhamento (encerrar pedido')
        print('1 - 200g de arroz')
        print('2 - 150g de farofa especial')                                  #SAIDA COM O MENU PARA O USUARIO ESCOLHER OS ADICIONAIS
        print('3 - 100g de couve cozida')
        print('4 - 1 laranja descascada')

        try:
            opçao_feijoada = int(input(''))  #ENTRADA DA OPÇÃO DESEJADA PELO USUARIO
            valor = 0  #VARIAVEL PARA SABER O VALOR DOS ADICIONAIS

            if opçao_feijoada == 1:
                valor += 5  #VALOR DO ADICIONAL ESCOLHIDO
                valor_acom = valor_acom + valor  #VALOR TOTALIZADO DOS ADICIONAIS ESCOLHIDOS
                continue

            elif opçao_feijoada == 2:
                valor += 6  #VALOR DO ADICIONAL ESCOLHIDO
                valor_acom = valor_acom + valor  #VALOR TOTALIZADO DOS ADICIONAIS ESCOLHIDOS
                continue

            elif opçao_feijoada == 3:                                  #FUNÇÃO PARA SABER QUAL ADICIONAL O USUARIO ESCOLHEU
                valor += 7  #VALOR DO ADICIONAL ESCOLHIDO
                valor_acom = valor_acom + valor  #VALOR TOTALIZADO DOS ADICIONAIS ESCOLHIDOS
                continue

            elif opçao_feijoada == 4:
                valor += 3  #VALOR DO ADICIONAL ESCOLHIDOV
                valor_acom = valor_acom + valor  #VALOR TOTALIZADO DOS ADICIONAIS ESCOLHIDOS
                continue
            
            elif opçao_feijoada == 0: #FUNÇÃO PARA QUANDO O USUARIO ENTRAR COM O VALOR SEJA FINALIZADO A ETAPA DE ADIOCIONAIS
                return valor_acom

            else:
                print('Você não digitou uma opção válida')  #ENTRADA CASO O USUARIO ENTRE COM UM OPÇÃO QUE NÃO TENHA NO MENU
                continue

        except ValueError:  #FUNÇÃO PARA CASO O USUARIO NÃO DIGITE UM VALOR NUMERICO
                print('Você não digitou uma opção válida')  #SAIDA CASO O USUARIO NÃO DIGITE UM VALOR NUMERICO
                continue

#principal

print('Bem-Vindo ao programa de Feijoada do Julio Cesar Ribeiro Lopes')  #NOME DO PROGRAMA

valor_volu = 0   #VARIAVEL PARA RECEBER O VALOR DEFINIDO PELO TAMANHO DA FEIJOADA
valor_feijoada = 0   #VARIAVEL PARA RECEBER O VALOR DO TIPO DE FEIJOADA ESCOLHIDA
valor_acom = 0   #VARIAVEL PARA RECEBER O VALOR DOS ACOMPANHAMENTOS DA FEIJOADA ESCOLHIDO

valor_volu = volumeFeijoada(valor_volu)   #VALOR DA FEIJOADA DEFINIDO PELO TAMANHO ESCOLHIDO
valor_feijoada = opcaoFeijoada(valor_feijoada)  #VALOR DO TIPO DE FEIJOADA ESCOLHIDO
valor_acom = acompanhamentoFeijoada(valor_acom)  #VALOR DOS ACOMPANHAMENTOS ESCOLHIDOS

print('Valor a ser pago é (R$): {} (volume = {} * opção = {} + acompanhamento = {}'.format(valor_volu * valor_feijoada + valor_acom, valor_volu, valor_feijoada, valor_acom))
                                                                                                                                    #SAIDA COM OS VALORES DA FEIJOADA ESCOLHIDA