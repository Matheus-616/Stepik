'''

[2.5 pontos] Escreva uma função sobrepostos  que:

    Receba como parâmetros 3 nomes de arquivos: A, B e C;
    Leia os conteúdos do arquivo A, que contém uma lista de números inteiros;
    Leia os conteúdos do arquivo B, que contém uma segunda lista de números inteiros ;
    Escreva no arquivo C apenas os números presentes no arquivo A e B, em ordem crescente;
    Ignore itens repetidos em um mesmo arquivo.

Cabeçalho da função:

def sobrepostos(A, B, C):

Não se preocupe com a chamada da função, ou impressão dos resultados, isso será feito automaticamente.
Escreva apenas a função solicitada.

Os exemplos de entrada e saída contêm possíveis conteúdos de arquivos a serem usados como entrada e esperados como saída.
As linhas que começam com # servem apenas para identificar o nome do arquivo e não fazem parte do arquivo em si.

'''

def sobrepostos(A, B, C):    
    listaA = open(A)
    listaB = open(B)
    listaC = open(C, 'w')
    lA = listaA.read().split('\n')
    lB = listaB.read().split('\n')
    if '' in lA:
        del lA[-1]
    lC = []
    for i in lA:
        if i in lB:
            if int(i) not in lC:
                lC.append(int(i))
    lC.sort()
    for i in lC:
        listaC.write('%d' % i)
        if i != lC[-1]:
            listaC.write('\n')
    return listaC
