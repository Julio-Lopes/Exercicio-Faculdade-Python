print('Bem-Vindo a Pizzaria do Julio Cesar Ribeiro Lopes')  #NOME DO PROGRAMA
print('_' * 22,'Cardapio', '_' * 22)
print('| Codigo |', ' Descrição  |', ' Pizza Media |', 'Pizza grande |' )
print('| 21     |', ' Napolitana |', ' R$ 20,00    |', 'R$ 26,00     |' )
print('| 22     |', ' Margherita |', ' R$ 20,00    |', 'R$ 26,00     |' )
print('| 23     |', ' Calabresa  |', ' R$ 25,00    |', 'R$ 32,50     |' )   #SAIDA COM O CARDAPIO
print('| 24     |', ' Toscana    |', ' R$ 30,00    |', 'R$ 39,00     |' )
print('| 25     |', ' Portuguesa |', ' R$ 30,00    |', 'R$ 39,00     |' )
print('_' * 54)
print()

total_final = 0  #VARIAVEL PARA SABER O TOTAL FINAL
while True:
    media = 0  #VARIAVEL PARA SABER A MEDIA
    total = 0  #VARIAVEL PARA SABER O TOTAL
    
    tam_piz = str(input('qual tamanho de pizza que deseja (M/G): ')).upper()  #ENTRADA PARA SABER O TAMANHO DA PIZZA (M= MEDIA) (G = GRANDE)
    if tam_piz == 'M' or tam_piz == 'G':  #FUNÇÃO PARA SABER O VALOR DA PIZZA PEQUENA OU GRANDE
        if tam_piz == 'M':
           tam_piz = 0  #VARIAVEL PARA CALCULAR MEDIA E SABER O VALOR FINAL DA PIZZA

        if tam_piz == 'G':
           tam_piz = 30 #VARIAVEL PARA CALCULAR MEDIA E SABER O VALOR FINAL DA PIZZA

    else:
        print('Opção invalida')  #SAIDA CASO O USUARIO DIGITE UMA OPÇÃO DIFERENTE DE (M/G)
        continue
    
    cod_prod = int(input('entre com o codigo do produto: '))  #ENTRADA DO CODIGO DA PIZZA DESCRITO NO MENU
    if cod_prod == 21 or cod_prod == 22 or cod_prod == 23 or cod_prod == 24 or cod_prod == 25:  #FUNÇÃO PARA SABER QUAL PIZZA O USUARIO ESCOLHEU
        if cod_prod == 21:
            cod_prod = 20
            print('Voce pediu uma pizza Napolitana')  #SAIDA COM O NOME DA PIZZA ESCOLHIDA PELO USUARIO
            

        elif cod_prod == 22:
            cod_prod = 20  #VARIAVEL COM O PREÇO DA PIZZA
            print('Voce pediu uma pizza Margherita')   #SAIDA COM O NOME DA PIZZA ESCOLHIDA PELO USUARIO

        elif cod_prod == 23:
            cod_prod = 25  #VARIAVEL COM O PREÇO DA PIZZA
            print('Voce pediu uma pizza Calabresa')   #SAIDA COM O NOME DA PIZZA ESCOLHIDA PELO USUARIO
                

        elif cod_prod == 24:
           cod_prod = 30   #VARIAVEL COM O PREÇO DA PIZZA
           print('Voce pediu uma Pizza Toscana')   #SAIDA COM O NOME DA PIZZA ESCOLHIDA PELO USUARIO
                

        elif cod_prod == 25:
           cod_prod = 30   #VARIAVEL COM O PREÇO DA PIZZA
           print('Voce pediu uma Pizza Portuguesa')   #SAIDA COM O NOME DA PIZZA ESCOLHIDA PELO USUARIO

    else:
        print('Opção invalida')   #SAIDA CASO O USUARIO ESCOLHA UMA OPÇÃO QUE NÃO ESTEJA NO CARDAPIO
        continue

    media = cod_prod*tam_piz/100  
    total = cod_prod + media           #CALCULO PARA SABER O VALOR TOTAL DA PIZZA
    total_final += total     #CALCULO PARA SABER O VALOR FINAL DE TODOS AS PIZZAS ESCOLHIDA PELO USUARIO
    
    print('Deseja pedir mais alguma coisa? ')
    print('1 - sim')                                   #SAIDA PARA PERGUNTA SE O USUARIO DESEJA FAZER MAIS UM PEDIDO
    print('0 - não')
    while True:  #FUNÇÃO PARA FORÇAR O USUARIO A DIGITA 0 OU 1
        finalizar = int(input())  #ENTRADA PARA SABER A OPÇÃO ESCOLHIDA PELO USUARIO SENDO 0 OU 1
        if finalizar == 1 or finalizar == 0:
            break
        else:
            print('opção invalida')  #SAIDA CASO O USUARIO NÃO DIGITE 0 OU 1
            continue
    if finalizar == 1:   #FUNÇAO PARA QUE O USUARIO FAÇA OUTRO PEDIDO
        continue
    else:  #FUNÇAO PARA SAIR DO LOOP
        break   

print('O total a ser pago é: {}'.format(total_final))  #SAIDA COM O VALOR TOTAL DE TODAS AS PIZZAS PEDIDAS PELO O USUARIO