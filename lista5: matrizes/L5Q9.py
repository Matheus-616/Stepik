'''

Dado um tabuleiro N×M  de batalha naval (1 = navio, 0 = agua) e uma sequencia de T tiros (x,y), calcule se todos os navios foram destruídos ou não (para um navio ser destruído, todas casas do tabuleiro das quais ele ocupa devem ser atingidas).

'''

n, m, t = (int(i) for i in input().split())
tabuleiro = []
tiros = []
c = 0
for i in range(n):
    tabuleiro.append([int(i) for i in input().split()])
for i in range(t):
    tiros.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(m):
        for k in range(t):
            if i == tiros[k][0] and j == tiros[k][1]:
                tabuleiro[i][j] = 0
        if tabuleiro[i][j] == 0:
            c += 1
if c == n*m:
    print('S')
else:
    print('N')
