x = int(input('valor do 1 lado: '))
y = int(input('valor do 2 lado: '))
z = int(input('valor do 3 lado: '))

if (x > 0 and y > 0 and z > 0):
    if(x + y > z and x + z > y and y + z > x):
        if(x != y and x != z and y != z ):
            print('é um triangulo escaleno')
        else:
            if(x == y and x==z):
                print('é um triangulo equilatero')
            else:
                print('é um triangulo isosceles')

    else:
     print('numeros invalidos')
else:
 print('numeros invalidos')           
