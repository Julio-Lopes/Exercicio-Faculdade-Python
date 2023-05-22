x = float(input('insira um numero: '))
y = float(input('insira um numero: '))
z = input('insira o tipo de calculo: ')

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

else:
    print('operacao invalida')
