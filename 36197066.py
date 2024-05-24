def string_para_matriz(texto,l,c):
    matriz = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(c):
            matriz[i][j] = texto[i * l + j]

    return matriz

def encontrar(str,nomes):
  if str.find(nomes) != -1 or str[::-1].find(nomes) != -1:
    return True
  else:
    return False




n, m, p = map(int, input().split())
nomes = [input().strip() for _ in range(n)]
matriz = [input().strip() for _ in range(m)]


#ZONA DE TESTE
#linha central
indice_i =0
indice_j = 0

str_lat = ''
index =0
ultimo = 0
principal = True

strCIMA = ''
strCentro =''
strBaixo = ''

while(True):
  if(index ==m):
    break
  try:
      str_lat += matriz[indice_i][indice_j]
      indice_j +=1
      indice_i +=1
  except IndexError:
    if(principal):
      strCentro = str_lat
      principal = False
    indice_i = 0
    indice_j = ultimo +1
    ultimo +=1
    index +=1

strCima = str_lat

indice_i =1
indice_j = 0
ultimo = 0
str_lat = ''
index = 0
while(True):
  if(index ==m):
    break
  try:
      str_lat += matriz[indice_i][indice_j]
      indice_j +=1
      indice_i +=1
  except IndexError:
    indice_i = ultimo+1
    indice_j = 0
    ultimo +=1
    index +=1
strBaixo = str_lat


for nome in nomes:
  if(encontrar(strCentro.lower(),nome)):
    print('1 Palavra "{}" na diagonal principal'.format(nome))
  elif(encontrar(strCima.lower(),nome)):
    print('2 Palavra "{}" acima da diagonal principal'.format(nome))
  elif(encontrar(strBaixo.lower(),nome)):
    print('3 Palavra "{}" abaixo da diagonal principal'.format(nome))
  else:
    print('4 Palavra "{}" inexistente'.format(nome))
