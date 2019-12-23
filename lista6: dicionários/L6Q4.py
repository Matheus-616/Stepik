'''

[1 ponto] Dois jogadores estão jogando um jogo de cartas. Neste jogo cada jogador tem um monte de N cartas a sua frente, em cada turno cada jogador vira a carta do topo do seu monte e vence o turno aquele que virou a maior carta. Vence o jogo o jogador que ganhou mais turnos. Escreva um programa que dados os dois montes de N cartas, calcule o jogador ganhador.

A comparação de duas cartas segue o seguinte critério:

- se as cartas são do mesmo naipe vence a carta de maior "numero" seguindo esta sequencia crescente:

2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < J < Q < K < A

- se os naipes são diferentes, vence o maior naipe seguindo esta sequencia:

ouros < espadas < copas < paus

A entrada do problema sera dada por duas linhas, cada uma contendo as N cartas de cada jogador seguindo o seguinte formato:

numero1 naipe1 numero2 naipe2 ... numeroN naipeN

Os jogadores retiram as cartas começando da primeira para a ultima, ou seja, o primeiro turno sera composto de (numero1 naipe1 do jogador 1) e (numero1 naipe1 do jogador 2), o segundo turno das cartas (numero2 naipe2 do jogador 1) e (numero2 naipe2 do jogador 2).

Imprima 1 se o jogador 1 venceu o jogo, 2 se o jogador 2 venceu e 0 se houve empate. (note que as cartas serão totalmente aleatórias e poderá acontecer de uma mesma carta aparecer mais de uma vez em cada monte)

Os números das cartas serão representados por

2 3 4 5 6 7 8 9 10 J Q K A

e os naipes por

ouros paus copas espadas

'''

jog1 = [i for i in input().split()]
jog2 = [i for i in input().split()]
c1 =0
c2 =0
for i in range(0,len(jog1),2):
    if jog1[i+1] != jog2[i+1]:
        if jog1[i+1] == 'paus':
            c1 += 1
        elif jog1[i+1] == 'copas':
            if jog2[i+1] == 'ouros' or jog2[i+1] == 'espadas':
                c1 += 1
            else:
                c2 += 1
        elif jog1[i+1] == 'espadas':
            if jog2[i+1] == 'ouros':
                c1 += 1
            else:
                c2 += 1
        else:
            c2 += 1
    else:
        if jog1[i] == 'J' or jog1[i] == 'Q' or jog1[i] == 'K'  or jog1[i] == 'A':
            if jog2[i] != 'J' and jog2[i] != 'Q' and jog2[i] != 'K'  and jog2[i] != 'A':
                c1 += 1
            elif jog1[i] != jog2[i]:
                if jog1[i] == 'A':
                    c1 += 1
                elif jog1[i] == 'K':
                    if jog2[i] == 'Q' or jog2[i] == 'Q':
                        c1 += 1
                    else:
                        c2 += 1
                elif jog1[i] == 'Q':
                    if jog2[i] == 'J':
                        c1 += 1
                    else:
                        c2 += 1
                else:
                    c2 += 1 
        else:
            if jog2[i] == 'J' or jog2[i] == 'Q' or jog2[i] == 'K'  or jog2[i] == 'A':
                c2+=1
            else:
                if int(jog2[i]) < int(jog1[i]):
                    c1 += 1
                elif int(jog2[i]) > int(jog1[i]):
                    c2+=1
if c1>c2:
    print(1)
elif c1<c2:
    print(2)
else:
    print(0)
