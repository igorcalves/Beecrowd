
qtd_frutas, qtd_linhas = map(int, input().split())
nomes = ['']*qtd_frutas
linhas = ['']*qtd_linhas
for i in range(qtd_frutas):
  nomes[i] = input().lower()

for x in range(qtd_linhas):
  linhas[x] = input().lower()
for nome in nomes:
  tem = 0
  for c in range(qtd_linhas):
    if(linhas[c].find(nome) != -1):
      tem = 1
    else:
      lt = linhas[c][::-1]
      if(lt.find(nome) != -1):
        tem = 1
  if(tem == 1):
    print('Sheldon come a fruta {}'.format(nome))
  else:
    print('Sheldon detesta a fruta {}'.format(nome))