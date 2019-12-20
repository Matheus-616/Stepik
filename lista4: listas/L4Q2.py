'''
Faça um programa que leia um vetor de n n n posições com números aleatórios entre 0 e 20.
O programa deve manipular os valores de cada posição do vetor fazendo um shift para a direita. Além disso, o vetor deve ser considerado circular, ou seja, o valor da última célula passa a ser o valor da primeira. 
'''

vetor = input().split()
aux = vetor[-1]
for i in range(len(vetor)-1,-1,-1):
        vetor[i] = vetor[i-1]
vetor[0] = aux
print(' '.join(vetor))
