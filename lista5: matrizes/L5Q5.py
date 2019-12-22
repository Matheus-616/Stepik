'''

Faça um programa que leia a ordem n n n (ímpar) de uma matriz quadrada, a matriz, e verifique se ela representa um Quadrado Mágico.
Imprima a soma de uma das linhas ou colunas caso a matriz seja um quadrado mágico, ou  -1 caso contrário.

'''

n = int(input())
matriz = []
s1 = 0
s2 = 0
s3 = 0
s4 = 0
diag1 = 0
diag2 = 0
a = 0
for i in range(n):
    matriz.append([int(i) for i in input().split()])
for i in range(n-1):
    s1 = 0
    s2 = 0
    for j in range(n):
        s1 += matriz[i][j]
        s2 += matriz[i+1][j]
        s3 += matriz[j][i]
        s4 += matriz[j][i+1]
        if i == 0:
            diag1 += matriz[j][j]
            diag2 += matriz[j][n-1-j]
    a = diag1
    if s1 != s2 or s3 != s4 or s1 != s2 or diag1 != diag2 or s1 != diag1:
        a = -1
        break 
print(a)
