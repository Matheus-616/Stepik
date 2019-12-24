'''

[2.5 pontos] Escreva uma função contagem  que:

    Receba como parâmetro o nome de um arquivo;
    Conte o número de palavras e linhas no arquivo;
    Retorne os resultados em uma tupla (palavras, linhas).

Cabeçalho da função:

def contagem(arquivo):

Não se preocupe com a chamada da função, ou impressão dos resultados, isso será feito automaticamente.
Escreva apenas a função solicitada.

Os exemplos de entrada e saída contêm possíveis conteúdos de arquivos a serem usados como entrada e esperados como saída.
As linhas que começam com # servem apenas para identificar o nome do arquivo e não fazem parte do arquivo em si.

'''

def contagem(arquivo):
    c = 0
    arqui = open(arquivo)
    lista = ([i for i in arqui.read().split('\n')])
    if '' == lista[-1]:
        del lista[-1]
    
    for j in range(len(lista)):
        lista[j] = lista[j].replace(","," ")
        lista[j] = lista[j].replace("."," ")
        lista[j] = lista[j].replace("?"," ")
        lista[j] = lista[j].replace("!"," ")
        lista[j] = lista[j].replace(";"," ")
        lista[j] = lista[j].replace(":"," ")
    for i in lista:
        l = i.split()
        for j in l:
            c += 1
    return (c, len(lista))
