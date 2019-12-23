'''

[2 pontos] Escreva um programa que busque palavras em um texto. O texto onde as palavras deverão ser buscadas é representado por uma única string (sem quebras de linhas). Para cada palavra a ser buscada o programa deverá imprimir a posição de todas ocorrências no texto. A posição de uma palavra é definida da seguinte forma: Digamos que uma palavra ocorre nas posições 3 e 7, então ela é a terceira e sétima palavras do texto.

Exemplo:

Para o texto "Eu não gosto de exercícios de geometria.", temos os resultados para as seguintes buscas:

"eu": 1 (primeira palavra)

"geometria" -> 7 (sétima palavra)

"de" -> 4 6 (quarta e sexta palavras)


A primeira linha do caso de entrada contém o texto do qual as palavras deverão ser buscadas.

A segunda linha contém um inteiro N indicando que haverão N buscas.

Cada uma das próximas N linhas conterá uma palavra a ser buscada.


Imprima para cada busca uma linha contendo as posições das ocorrências da palavra. Se a palavra nao existe no texto, imprima o caractere '-'. (atentos aos pontos e virgulas, e lembrando que neste problema as posicoes comecam de 1)


'''

frase = input().split()
for i in range(len(frase)):
    frase[i] = frase[i].lower()
    frase[i] = frase[i].replace('.', '')
    frase[i] = frase[i].replace(',', '')
    frase[i] = frase[i].replace('!', '')
    frase[i] = frase[i].replace('?', '')
n = int(input())
busca = []
for i in range(n):
    busca.append(input().lower())
for j in range(len(busca)):
    p = []
    for i in range(len(frase)):
        if busca[j] == frase[i]:
            p.append(str(i+1))
    print('-' if p == [] else ' '.join(p))
