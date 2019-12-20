'''
Escreva um programa que receba um passo de tempo Δt, um numero  M  de passos de simulação e uma lista com n partículas com posição inicial e velocidade.
Considerando as velocidades constantes e ignorando colisões, o seu programa deve calcular a posição final de cada partícula utilizando o método de integração explicito de Euler: 

'''

t, m, n = input().split()
t, m, n = float(t), int(m), int(n)
lista = []
lista1 = []
for i in range(n):
    lista = [float(i) for i in input().split()]
    lista1.append(lista)
for i in lista1:
    print('%.2f %.2f %.2f'% (i[0]+m*i[3]*t, i[1]+m*i[4]*t, i[2]+m*i[5]*t))
