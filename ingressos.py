total = 0
ingresso = 0
ig = 0

while True:
   idade = input('insira a idade do seu cliente ou digite sair: ')
   if (idade == 'sair'):
    break
   idade = int(idade)
   ingresso += 1

   if(idade <= 3):
    print('seu ingresso sera de graça :)')
    
   elif(idade <= 12):
      ig += 15
      print('seu ingresso custara 15RS reais')
      
   elif(idade > 12):
      ig += 30
      print('seu ingresso custara 30RS reais')
   
   total += ig
   media = total / ingresso
   
print('total de ingressos vendidos {}, total ganho com ingressos {}RS , media de idade {} '.format(ingresso,total,media))    