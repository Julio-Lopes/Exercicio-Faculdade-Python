print('Bem Vindo a Loja do Julio Cesar Ribeiro Lopes')  #NOME DO PROGRAMA

valor_un = float(input('entre com o valor do produto: '))   #ENTRADA DO VALOR UNITARIO
quant_prod = int(input('entre com o valor da quantidade: '))   #ENTRADA DA QUANTIDADE DO PRODUTO
valor_total = valor_un * quant_prod   #CALCULO PARA SABER O VALOR TOTAL SEM O DESCONTO

if quant_prod <= 4:  #SE A QUANTIDADE DO PRODUTO FOR MENOR OU IGUAL A 4 CAIRA NESSA FUNÇÃO
    print('o valor sem desconto foi: R$ {}'.format(valor_total))  #SAIDA COM VALOR SEM DESCONTO
    valor_desc = valor_total*0/100  #CALCULO PARA SABER O DESCONTO
    print('o valor sem desconto foi: R$ {}  (desconto 0%)'.format(valor_total-valor_desc))  #SAIDA COM VALOR COM DESCONTO

elif quant_prod <= 19:  #SE A QUANTIDADE DO PRODUTO FOR MENOR OU IGUAL A 19 CAIRA NESSA FUNÇÃO
    print('o valor sem desconto foi: R$ {}'.format(valor_total))  #SAIDA COM VALOR SEM DESCONTO
    valor_desc = valor_total*3/100  #CALCULO PARA SABER O DESCONTO
    print('o valor sem desconto foi: R$ {}  (desconto 3%)'.format(valor_total-valor_desc))  #SAIDA COM VALOR COM DESCONTO

elif quant_prod <= 99:  #SE A QUANTIDADE DO PRODUTO FOR MENOR OU IGUAL A 99 CAIRA NESSA FUNÇÃO
    print('o valor sem desconto foi: R$ {}'.format(valor_total))  #SAIDA COM VALOR SEM DESCONTO
    valor_desc = valor_total*6/100  #CALCULO PARA SABER O DESCONTO
    print('o valor sem desconto foi: R$ {}  (desconto 6%)'.format(valor_total-valor_desc))  #SAIDA COM VALOR COM DESCONTO

else:  #SE A QUANTIDADE DO PRODUTO FOR IGUAL OU SUPERIOR A 100 CAIRA NESSA FUNÇÃO
    print('o valor sem desconto foi: R$ {}'.format(valor_total))  #SAIDA COM VALOR SEM DESCONTO
    valor_desc = valor_total*10/100  #CALCULO PARA SABER O DESCONTO
    print('o valor sem desconto foi: R$ {}  (desconto 10%)'.format(valor_total-valor_desc))  #SAIDA COM VALOR COM DESCONTO