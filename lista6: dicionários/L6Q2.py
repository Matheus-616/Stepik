'''

[1 ponto] Uma molécula de RNA mensageiro é utilizada como base na síntese de proteínas, num processo denominado de tradução.
Uma trinca de bases RNA corresponde a um aminoácido na proteína a ser produzida pela combinação ordenada dos aminoácidos.

Faça um programa que leia uma sequência de bases de uma molécula de RNA mensageiro, e realize a sua tradução para a sequência de aminoácidos de acordo com a tabela simplificada abaixo: [Tabela no outro arquivo]

'''

dic = {'UUU':'Phe','CUU':'Leu','UUA':'Leu','AAG':'Lis','UCU':'Ser','UAU':'Tyr','CAA':'Gln'}
seq = input()
final = []
for i in range(0,len(seq),3):
    final.append(dic[seq[i]+seq[i+1]+seq[i+2]])
print('-'.join(final))
