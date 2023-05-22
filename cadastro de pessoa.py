pessoa = {}
lista = []
soma = media = 0
while True:
    pessoa.clear
    resp = input('deseja cadastrar uma pessoa ? [S/N]')
    if resp == 'n':
        break
    pessoa['nome'] = str(input('NOME: '))
    pessoa['sexo'] = str(input('SEXO: [M/F] ')).upper()
    pessoa['ano'] = 2022 - int(input('ANO DE NASCIMENTO: '))
    soma += pessoa['ano']
    lista.append(pessoa.copy())

print()

print('o total de pessoas cadastrada é: {}'.format(len(lista)))
print()

media = soma / len(lista)
print('a MEDIA da IDADE das PESSOAS é: {}'.format(media))
print()

print('as mulheres com menos de 30 anos cadastradas foram: ' , end = '')
for i in lista:
    if i['sexo'] in 'fF' and i['ano'] <= 30:
        print(i['nome'])
print()

print('os homens com mais de 30 anos cadastrados foram: ' , end = '')
for p in lista:
    if p['sexo'] in 'Mm' and p['ano'] > 30:
        print(p['nome'])
print()