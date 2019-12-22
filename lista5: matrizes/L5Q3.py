#Faça um programa que leia uma matriz quadrada A de ordem 2. Se A for invertível, calcule e imprima a sua inversa B=A−1. Caso contrário, imprima "Singular". 

matriz = []
for i in range(2):
    matriz.append([float(i) for i in input().split()])
det = matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0]
if det == 0:
    print('Singular')
else:
    i = matriz[0][0]
    matriz[0][0] = (-1)**(1+1)*matriz[1][1]
    matriz[0][1] = (-1)**(1+2)*matriz[0][1]
    matriz[1][0] = (-1)**(2+1)*matriz[1][0]
    matriz[1][1] = (-1)**(2+2)*i
    for i in range(2):
        for j in range(2):
            matriz[i][j] = ('%.2f' % ((1/det)*matriz[i][j]))
    for i in range(2):
        print(' '.join(matriz[i]))   


