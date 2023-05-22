def fato (x):
 y = 1

 if (x == 0):
    print(y) 
   
 for i in range (1, x + 1,1):
    y *= i
    print(y)

x = int(input('insira um numero: '))
print(fato(x))