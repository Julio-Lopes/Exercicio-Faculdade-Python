while True:
    z = input('insira o tipo de calculo ou digite sair: ')
    if(z == '+'or z == '-' or z == '*' or z == '/'):
       x = float(input('insira um numero: '))
       y = float(input('insira um numero: '))

    if (z == '+'):
        res = x + y
        print('{} + {} = {}'.format(x,y,res) )

    elif(z == '-'):
        res = x - y
        print('{} - {} = {}'.format(x,y,res) )

    elif(z == '*'):
        res = x * y
        print('{} * {} = {}'.format(x,y,res) )

    elif(z == '/'):
        res = x / y
        print('{} / {} = {}'.format(x,y,res) )
    elif(z == 'sair'):
        break
    else:
        print('operaçao invalida')
    continue