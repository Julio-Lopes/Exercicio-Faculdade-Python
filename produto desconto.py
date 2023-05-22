i = str(input('qual o nome do produto ?'))
x = float(input('qual o valor do produto ?'))
y = float(input ('qual o percentual do desconto?'))
o = x*y/100
res= ('o produto {} custa {} com o desconto de {}% fica a {}').format(i, x ,y, x-o )
print(res)