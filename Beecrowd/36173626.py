
def menor_valor(ordem):
    i = -1
    index = False
    menor = ordem[0]; 
    for x in (ordem):
        i += 1
        if x < menor:
            menor = x
            index = i
    del ordem[index]
    return menor
valor1,valor2,valor3 = map(int, input().split()) 


ordem = [valor1,valor2,valor3]
copia = [valor1,valor2,valor3]
ordenado  = [menor_valor(ordem)]

if(ordem[0]<ordem[1]):
  ordenado.append(ordem[0])
  ordenado.append(ordem[1])
else:
  ordenado.append(ordem[1])
  ordenado.append(ordem[0])

for x in ordenado:
  print(x)
print()
for j in copia:
  print(j)