km = float(input('insira quantidade de KM percorrida '))
d = int(input('insira quantos dias o carro foi alugado'))
preco = 60 * d + 0.15 * km

print('carro foi alugado por {} dias e percorreu {} km, o valor a ser pago pelo aluguel do carro é {} reais' .format(d, km, preco) )