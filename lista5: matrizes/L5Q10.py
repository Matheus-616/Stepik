'''

Dada uma matriz A A A de tamanho m×n m \times n m×n, definimos uma "ampulheta" na matriz um pedaço de A A A no qual os elementos se dispõem na seguinte maneira:

a b c
  d 
e f g


Faça um programa que calcule a ampulheta com a maior soma de seus elementos. 

'''
n, m = (int(i) for i in input().split())
matriz = []
for i in range(n):
    matriz.append([int(i) for i in input().split()])
maxi = 0
for i in range(n-2):
    for j in range(m-2):
        soma = matriz[i][j]+matriz[i][j+1]+matriz[i][j+2]+matriz[i+1][j+1]+matriz[i+2][j]+matriz[i+2][j+1]+matriz[i+2][j+2]
        if soma > maxi:
            maxi = soma
print(maxi)
