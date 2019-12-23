'''

[2 pontos] O jogo do caça palavras: Dado uma matriz de dimensões NxM, informe se uma palavra existe na matriz. A palavra pode ser construída de letras em células sequencialmente adjacentes, ou seja, aquelas células vizinhas horizontalmente ou verticalmente. Uma mesma célula não pode ser utilizada mais de uma vez. Por exemplo:

P B C E
S U C S
A D E E

palavra = "PBCCED", retorna Sim,
palavra = "USP", retorna Sim,
palavra = "PBCB", retorna Não.

O algoritmo deve receber uma matriz, de dimensão NxM, a quantidade de palvras a procurar e as palavras, como pode-se observar no caso de teste. A saida do algoritmo deve ser a palavra  "Sim" se a palavra existir na Matriz e "Não" caso contrario.

A função Search deve fazer a busca da palavra, e pode ser definida da seguinte maneira:

def Search(i,j,k,word,Used):

Onde i e j são os índices da matriz que está sendo processada, k o índice da letra atual que está procurando da palavra word e a matriz auxiliar Used,  que marca as posições da matriz que foram usados.

A função Search deve ser chamada no seu código principal que pode ter o seguinte aspecto.

'''

#Nessa questão foi necessário criar o programa completo

def Search(i,j,k,word,Used):
    Used.append([i,j])
    if k == len(word):
        return True
    else: 
        if matriz[i-1][j] == word[k] and ([i-1,j] not in Used):
            if Search(i-1, j, k+1,word, Used):
                return True
        if matriz[i][j-1] == word[k] and ([i,j-1] not in Used):
            if Search(i, j-1, k+1,word, Used):
                return True
        if matriz[i][j+1] == word[k] and ([i,j+1] not in Used):
            if Search(i, j+1, k+1,word, Used):
                return True
        if matriz[i+1][j] == word[k] and ([i+1,j] not in Used):
            if Search(i+1, j, k+1,word, Used):
                return True
    Used.clear()   
n, m = input().split()
n, m = int(n), int(m)
matriz = []
busca = []
Used = []
for i in range(n):
    matriz.append(input().split())
matriz.insert(0,[0]*m)
matriz.append([0]*m)
for i in range(len(matriz)):
    matriz[i].insert(0, 0)
    matriz[i].append(0)
b = int(input())
for i in range(b):
    busca.append(input())
for pal in busca:
    a = 0
    for i in range(1,n+1):
        for j in range(1, m+1):
            if matriz[i][j] == pal[0] and a == 0:
                if Search(i, j, 1,pal, Used):
                    print('Sim')
                    a = 1
    if a == 0:
        print('Não')
    Used.clear()
