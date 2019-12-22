#Faça um programa que leia duas matrizes quadradas A e B de ordem 2 e calcule C=A+B.

m1 = []
m2 = []
import numpy as np
for i in range(2):
    m1.append([float(j) for j in input().split()])
for i in range(2):
    m2.append([float(j) for j in input().split()])
m1 = np.array(m1)
m2 = np.array(m2)
m1 = m1 + m2
for i in range(2):
    print('%.2f %.2f' % (m1[i][0], m1[i][1]))

