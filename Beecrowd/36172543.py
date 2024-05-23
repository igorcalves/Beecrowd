x = int(input())

for i in range(x):
    lido = int(input())
    if(lido == 0):
        print('NULL')
    if(lido % 2) == 0:
        if(lido >0):
            print('EVEN POSITIVE')
        elif(lido<0):
            print('EVEN NEGATIVE')
    else:
        if(lido >0):
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')