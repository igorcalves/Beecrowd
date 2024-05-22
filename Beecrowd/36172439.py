def definir_impar_par(valor1, valor2):
    result = (valor1+valor2)
    if(result %2) == 0:
        return 1
    else:
        return 0



def cod(roubo, acusa, imp_ou_par):
    if(roubo == 0 and acusa == 0):
    #condição normal
        if(escolha == imp_ou_par):
            print('Jogador 1 ganha!')
        else:
            print("Jogador 2 ganha!")
    #condição normal
    elif(roubo == 1 and acusa == 0):
        print('Jogador 1 ganha!')
    elif(roubo == 1 and acusa == 1):
        print('Jogador 2 ganha!')
    elif(roubo == 0 and acusa == 1):
        print('Jogador 1 ganha!')

  
  
escolha, j1,j2, roubo, acusa = map(int, input().split()) 

imp_ou_par = definir_impar_par(j1,j2)
cod(roubo,acusa,imp_ou_par)
