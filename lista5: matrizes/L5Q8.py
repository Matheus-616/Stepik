'''

Faça um programa que leia um tabuleiro de jogo da velha e informe o resultado atual: 

    Velha: quando não há mais possibilidade de um dos jogadores vencer;
    X: quando o jogador X vencer;
    O: quando o jogador O vencer.

O tabuleiro representa um jogo completo, mas pode ter mais de um vencedor. No caso de dois vencedores preferir o jogador X, uma vez que ele é o primeiro a jogar. 

Dentro de uma linha, os elementos são separados por uma barra vertical: |. Os possíveis elementos são X para o jogador X, e O para o jogador O.

'''

jogo = []
ganho = []
for i in range(3):
    jogo.append([j for j in input().split('|')])
for i in range(3):
    x = 0
    o = 0
    for j in range(3):
        if jogo[i][j] == 'X':
            x +=1
        else:
            o += 1
    ganho.append([x, o])
for i in range(3):
    x = 0
    o = 0
    for j in range(3):
        if jogo[j][i] == 'X':
            x +=1
        else:
            o += 1
    ganho.append([x, o])
x = 0
o = 0
for i in range(3):
    if jogo[i][i] == 'X':
        x +=1
    else:
        o += 1
ganho.append([x,o])
x = 0
o = 0
for i in range(3):
    if jogo[2-i][i] == 'X':
        x +=1
    else:
        o += 1
ganho.append([x,o])
for i in range(8):
    if ganho[i][0] == 3 and x != 5:
        x = 5
    elif ganho[i][1] == 3 and o != 5:
        o = 5
if x == 5:
    print('X')
elif o == 5:
    print('O')
else:
    print('Velha')

