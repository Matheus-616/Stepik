#Escreva um programa que receba um vetor com n n n notas (0 a 10) de um trabalho e calcule: média, mediana e desvio padrão.

import numpy as np
notas = [float(i) for i in input().split()]
soma = 0
notas.sort()
for i in notas:
    soma += i
media = soma/(len(notas))
soma = 0
for i in notas:
    soma += (i-media)**2
dp = np.sqrt(soma/(len(notas))) 
if len(notas)%2 == 1:
    mediana = float(notas[int(len(notas)/2)])
else:
    mediana = (float(notas[int(len(notas)/2)]) + float(notas[int(len(notas)/2-1)]))/2
print('%.2f %.2f %.2f' % (media, mediana, dp))
