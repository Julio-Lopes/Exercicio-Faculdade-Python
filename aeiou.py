palavra = ('mario', 'luigi' , 'peach', 'eleven')

for palavra in palavra:
   print('\n palavra: {}. vogais: ' .format(palavra.upper()),end = ' ')
   for letra in palavra:
      if letra.lower() in 'aeiou':
         print(letra.upper(), end=' ')