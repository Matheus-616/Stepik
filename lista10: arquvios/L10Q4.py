'''

[2.5 pontos] Uma molécula de RNA mensageiro é utilizada como base na síntese de proteínas, num processo denominado de tradução.
Uma trinca de bases RNA corresponde a um aminoácido na proteína a ser produzida pela combinação ordenada dos aminoácidos.

Faça um função traducao_rna que receba um nome de arquivo de entrada e o nome de um arquivo de saída. Leia do arquivo de entrada uma sequência de bases de uma molécula de RNA mensageiro, e realize a sua tradução para a sequência de aminoácidos de acordo com a tabela simplificada abaixo: (tabela disponível na lista 6)
 

A sequência resultante da tradução deve ser escrita no arquivo de saída passado para a função.

Cabeçalho da função:

def traducao_rna(arquivo_entrada, arquivo_saida):

Não se preocupe com a chamada da função, ou impressão dos resultados, isso será feito automaticamente.
Escreva apenas a função solicitada.

Os exemplos de entrada e saída contêm possíveis conteúdos de arquivos a serem usados como entrada e esperados como saída.
As linhas que começam com # servem apenas para identificar o nome do arquivo e não fazem parte do arquivo em si.


'''

def traducao_rna(I, O):
    dic = {'UUU':'Phe', 'CUU':'Leu', 'UUA':'Leu', 'AAG':'Lis', 'UCU':'Ser', 'UAU':'Tyr', 'CAA':'Gln'}
    mensagem = open(I)
    prot = open(O,'w')
    lista = [i for i in mensagem.read()]
    del lista[-1]
    for i in range(0,len(lista),3):
        prot.write(dic['%s%s%s' %(lista[i],lista[i+1],lista[i+2])])
        if i < len(lista)-3:
            prot.write('-')
