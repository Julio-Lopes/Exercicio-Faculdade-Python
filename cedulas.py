while True:
    x = int(input('inisra um valor ou entre com 0 para sair: '))

    if (x >= 100):
       c100 = x // 100
       x -= c100 * 100
       print('cedulas de 100 : {}'.format(c100))
    if (x >= 50):
       c50 = x // 50
       x -= c100 * 50
       print('cedulas de 50 : {}'.format(c50))
    if (x >= 20):
       c20 = x // 20
       x -= c20 * 20
       print('cedulas de 20 : {}'.format(c20))
    if (x >= 10):
      c10 = x // 10
      x -= c10 * 10
      print('cedulas de 10 : {}'.format(c10))
    if (x >= 5):
      c5 = x // 5
      x -= c5 * 5
      print('cedulas de 5 : {}'.format(c5))
    if (x >= 1):
      c1 = x // 1
      x -= c1 * 1
      print('cedulas de 1 : {}'.format(c1))
    if(x == 0):
        break
    else:
        continue
        

    