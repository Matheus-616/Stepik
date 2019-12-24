'''

[2.5 pontos] Escreva uma função concat_horizontal  que:

    Receba como parâmetros 3 nomes de arquivos: A, B e C, e uma string a ser usada como separador;
    Leia os conteúdos do arquivo A;
    Leia os conteúdos do arquivo B;
    Escreva no arquivo C os conteúdos de A e B concatenados horizontalmente, utilizando o separador entre;
    Caso um dos arquivos possua menos linhas que o outro apenas adicione a C as linhas que sobrarem, sem separador.

Cabeçalho da função:

def concat_horizontal(A, B, C, separador):

Não se preocupe com a chamada da função, ou impressão dos resultados, isso será feito automaticamente.
Escreva apenas a função solicitada.

Os exemplos de entrada e saída contêm possíveis conteúdos de arquivos a serem usados como entrada e esperados como saída.
As linhas que começam com # servem apenas para identificar o nome do arquivo e não fazem parte do arquivo em si.


'''

def concat_horizontal(A, B, C, separador):  
    listaA = open(A)
    listaB = open(B)
    listaC = open(C, 'w')
    lA = listaA.read().split('\n')
    lB = listaB.read().split('\n')
    mi = min(len(lA),len(lB))
    mm = max(len(lA),len(lB))
    for i in range(mm):
        if i < mi-1:
            listaC.write("%s%s%s\n" % (lA[i],separador, lB[i]))
        elif len(lA) > len(lB):
            listaC.write('%s\n' % lA[i])
        elif len(lB)>len(lA):
            listaC.write('%s\n' % lB[i])
    return listaC
