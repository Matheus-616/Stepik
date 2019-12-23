'''

Nessa questão foi pedido para criar apenas duas funções para uma nova versão do jogo "Space Invaders", que segue as seguintes regras:

"Seu novo jogo é assim:

- Os inimigos são representados por círculos de tamanhos variados.

- Sua nave dispara raios que atingem todos os inimigos em seu caminho.

- Um inimigo é atingido se o raio intersecta seu círculo.

- Ao ser atingido,  o inimigo explode em 4 círculos menores que continuam no jogo. Porém, este processo acontece no máximo 2 vezes."

As funções pedidas foram:
	1ª) Dado a posição de onde o disparo saiu, o vetor que define sua direção, o centro de um círculo e seu raio, era pra informar se o círculo foi atingido, True para o caso de ser atingido e False caso não fosse atingido.
	2ª) Dada as coordenadas do centro e o raio de um círculo atingido, a função deveria retornar uma lista com as coordenadas dos centros dos 4 círculos filhos e seus raios

'''

def intersecta(x, y, vx, vy, cx, cy, r):        
    # PARÂMETROS: 1) a posição (x,y) e a direção (vx,vy) do raio laser disparado, 
    #             2) o centro (cx,cy) e o raio r de um círculo.
    # RETORNO: True caso o raio laser intersecte o círculo ou 
    #          False caso contrário.           
    # ------------------------------
    import numpy as np
    vx1 = vx/np.sqrt(vx**2+vy**2)
    vy1 = vy/np.sqrt(vx**2+vy**2)
    d = np.arange(0, 100, 0.1)
    for i in d:
        if (x+i*vx1-cx)**2 + (y+i*vy1-cy)**2 <= r**2:
                return True
    return False
    # ------------------------------

def explode(cx, cy, r):
    # PARÂMETROS: o centro (cx,cy) e o raio r de um círculo que será explodido.
    # RETORNO:  uma lista de 4 novos cículos com as seguintes propriedades
    #           1º círculo -> centro (cx + r, cy) e raio r/2
    #           2º círculo -> centro (cx - r, cy) e raio r/2
    #           3º círculo -> centro (cx, cy - r) e raio r/2
    #           4º círculo -> centro (cx, cy + r) e raio r/2
    # ------------------------------
     return [cx+r, cy, r/2, cx-r, cy, r/2, cx, cy-r, r/2, cx, cy+r, r/2]
    # ------------------------------

