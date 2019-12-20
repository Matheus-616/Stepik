'''Faça um programa que leia um vetor de n posições com valores entre 0 e 20 e encontre:

    1. A soma dos valores armazenados no vetor;
    2. O número de ocorrências do valor 9;
    3. O maior valor armazenado no vetor;
    4. As posições onde aparecem o maior valor encontrado no item 3. – note que aqui o programa possivelmente imprimirá mais de uma posição.'''

vetor = [int(i) for i in input().split()]
soma = 0
c = 0
maior = max(vetor)
lista = []
for i in range(len(vetor)):
    soma += vetor[i]
    if vetor[i] == 9:
        c += 1
    if vetor[i] == maior:
        lista.append(str(i))
print(soma)
print(c)
print(maior)
print(' '.join(lista))
