'''

[2 pontos] A ferramenta do baldinho de tinta:

existente em vários softwares de desenho (como o photoshop, paintbrush, etc...). Caso nunca tenha usado nada disso, o balde funciona da seguinte maneira: o usuário clica em um pixel da tela e ele "espalha" a nova cor dele por todos pixels da mesma cor original do pixel que estão conectados com o pixel clicado. Pixels conectados sao os vizinhos do pixel clicado, os vizinhos dos vizinhos e assim por diante. A vizinhança de um pixel e composta pelos 8 pixels vizinhos em sua volta.

Dada uma matriz M representando os pixels de uma imagem e as coordenadas x e y representando a coordenada do pixel em que o usuário clicou, a função quantidade(l, c, M) retorna a quantidade de pixels alterados pela operação do balde.

'''


def quantidade(l, c, M):
    d = 0
    e  = M[l][c]
    M.insert(0, len(M[0])*[-1])
    M.append(len(M[0])*[-1])
    for i in range(len(M)):
        M[i].insert(0, -1)
        M[i].append(-1)
    l += 1
    c += 1
    M = altera(l, c, e, M)
    for i in range(1,len(M)-1):
        for j in range(1,len(M[0])-1):
            if M[i][j] == 'a':
                d += 1
    return d

def altera(l, c, e, M):
    M[l][c] = 'a'
    for i in range(l-1,l+2):
        for j in range(c-1,c+2):
            if M[i][j] == e:
                M = altera(i, j, e, M)
    return M
