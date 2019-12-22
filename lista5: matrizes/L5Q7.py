'''

Dado um tabuleiro de xadrez com algumas rainhas, verifique se ao menos uma rainha pode matar a outra. (A rainha no xadrez pode caminhar em linha reta para todas as direções: horizontal, vertical e diagonal).

A entrada do problema e representada por uma matriz 8x8, onde 1 representa a matriz e 0 a casa vazia. Imprima 'S' caso alguma rainha consiga matar a outra e 'N' se todas estao seguras.

'''

campo =[]
for i in range(8):
    campo.append([int(i) for i in input().split()])
for i in range(8): # linhas
    a = 0
    for j in range(8):
        if campo[i][j] == 1:
            a += 1
        if a == 2:
            break
    if a == 2:
        break
if a != 2:    
    for i in range(8): # colunas
        a = 0
        for j in range(8):
            if campo[j][i] == 1:
                a +=1
            if a == 2:
                break
        if a == 2:
            break
if a != 2:            
    for i in range(8): #Diagonal 1
        a = 0
        for j in range(8-i):
                if campo[i+j][j] == 1:
                    a += 1
                if a == 2:
                    break
        if a == 2:
            break
if a != 2:    
    for i in range(8): #Diagonal 2
        a = 0
        for j in range(8-i):
                if campo[j][i+j] == 1:
                    a += 1
                if a == 2:
                    break
        if a == 2:
            break
if a != 2:            
    for i in range(7,-1,-1): #Diagonal 3
        a = 0
        for j in range(i+1):
                if campo[j][i-j] == 1:
                    a += 1
                if a == 2:
                    break
        if a == 2:
            break
if a != 2:            
    for i in range(8): #Diagonal 4
        a = 0
        for j in range(8-i):
                if campo[i+j][7-j] == 1:
                    a += 1
                if a == 2:
                    break
        if a == 2:
            break
if a == 2:
    print('S')
else:
    print('N')

