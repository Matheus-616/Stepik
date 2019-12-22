'''

O jogo Campo Minado constitui de uma matriz composta por bombas e números. Existem bombas espalhadas e cada casa do tabuleiro tem um numero que corresponde ao numero de bombas existentes em volta daquela casa (quantos dos seus 8 vizinhos são bombas). 

Dada a configuração inicial das bombas (1 = bomba, 0 = caso contrario) em um tabuleiro de tamanho N x M, imprima o tabuleiro completo com todos os números. Coloque -1 no lugar das bombas e 0 a 8 no restante. 

'''

n, m = input().split()
n, m = int(n)+1, int(m)+1
campo = []
campo.append((m+1)*[0])
for i in range(n-1):
    campo.append([int(k) for k in input().split()])
    campo[i+1].append(0)
    campo[i+1].insert(0, 0)
campo.append((m+1)*[0])

for i in range(1,n):
    for j in range(1, m):
        if campo[i][j] == 1:
            campo[i][j] = -1
        else:
            c = 0
            if campo[i-1][j-1] == -1:
                c += 1
            if campo[i-1][j] == -1:
                c += 1
            if campo[i-1][j+1] == -1:
                c += 1
            if campo[i][j-1] == -1:
                c += 1
            if campo[i][j+1] == 1:
                c += 1
            if campo[i+1][j-1] == 1:
                c += 1
            if campo[i+1][j] == 1:
                c += 1
            if campo[i+1][j+1] == 1:
                c += 1
            campo[i][j] = c
del campo[0]
del campo[n-1]
for i in range(n-1):
    del campo[i][0]
    del campo[i][m-1]
    for j in range(m-1):
        campo[i][j] = str(campo[i][j])
for i in range(0, n-1):
    print(' '.join(campo[i]))
