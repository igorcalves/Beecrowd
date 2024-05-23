valor = int(input())
print('{} ano(s)'.format((valor//365)))
print('{} mes(es)'.format((valor % 365) // 30))
print('{} dia(s)'.format((valor % 365) % 30))