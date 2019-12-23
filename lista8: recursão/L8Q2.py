'''

[1 ponto] Escreva uma função matriz_2x2_inversa: recebe uma matriz 2×2 e calcula a sua inversa. Retorne None caso a matriz seja singular.

Cabeçalho da função:

def matriz_2x2_inversa(M):


Não se preocupe com a chamada das funções, ou impressão dos resultados, isso será feito automaticamente.  
Escreva apenas as funções solicitadas.

'''

def matriz_2x2_inversa(M):
    det_M = M[0][0]*M[1][1]-M[0][1]*M[1][0]
    if det_M != 0:
        M1 = [[0,0],[0,0]]
        M1[0][0] = M[1][1]
        M1[0][1] = -M[0][1]
        M1[1][0] = -M[1][0]
        M1[1][1] = M[0][0]
        for i in range(2):
            for j in range(2):
                M1[i][j] *= 1/det_M
        return M1
