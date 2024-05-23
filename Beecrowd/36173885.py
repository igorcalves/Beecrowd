saida = ''
while(True):
  try:
    saida = input()
    if(int(saida) >=1):
      print('vai ter duas!')
    else:
      print('vai ter copa!')
  except EOFError:
    break