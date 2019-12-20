#Faça um programa que leia um vetor de n posições e inverta o vetor.
#Faça a inversão SEM usar um vetor auxiliar. Imprima o vetor invertido.

vetor = input().split()
vetor = vetor[len(vetor)::-1]
print(' '.join(vetor))
