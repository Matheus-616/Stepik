'''

Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes.

Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes e imprima resultante da multiplicação, ou 'Incompatíveis' caso contrário. 

'''

import numpy as np
l1, c1, l2, c2 = [int (i) for i in input().split()]
if c1 != l2:
    print('Incompatíveis')
else:
    matriz1 =[]
    matriz2 = []
    for i in range(l1):
        matriz1.append([float(j) for j in input().split()])
    for i in range(l2):
        matriz2.append([float(j) for j in input().split()])
    matriz1 = np.array(matriz1)
    matriz2 = np.array(matriz2)
    matriz = matriz1 @ matriz2
    for i in range(l1):
        d = []
        for j in range(c2):
            d.append('%.2f' % matriz[i][j])
        print(' '.join(d))
