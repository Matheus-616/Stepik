#Faça um programa que leia as dimensões de uma matriz A, e depois leia a própria matriz e calcule a sua transposta B=A^T . 

import numpy as np
l, c = input().split()
l, c = int(l), int(c)
matriz = []
matriz_t = []
for i in range(l):
    matriz.append([float(i) for i in input().split()])
for i in range(c):
    linha = []
    for j in range(l):
        linha.append('%.2f' % matriz[j][i])
    print(' '.join(linha)) 
