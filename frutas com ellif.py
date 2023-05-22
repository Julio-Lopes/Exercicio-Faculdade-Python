x = int(input('digite 1 para maça, 2 para laranja, 3 para banana: '))
un = int(input('digite a quantidade do produto: '))
if (x == 1):
    total = un * 2.3
    print('voce comprou {} maças e o total foi de {} reais'.format(un, total))
elif(x == 2):
    total = un * 3.6
    print('voce comprou {} laranjas e o total foi de {} reais'.format(un, total))
elif(x == 3):
        total = un * 1.85
        print('voce comprou {} bananas e o total foi de {} reais'.format(un, total))
else:
    print('numero invalido')
   