def menor_valor(ordem):
    i = -1
    index = False
    menor = ordem[0]; 
    for x in (ordem):
        i += 1
        if x > menor:
            menor = x
            index = i
    del ordem[index]
    return menor
valor1,valor2,valor3 = map(int, input().split()) 


ordem = [valor1,valor2,valor3]

print('{} eh o maior'.format(menor_valor(ordem)))