'''
Faça um programa que leia um vetor vet vet vet de 20 posições. O programa deve gerar, a partir do vetor lido, um outro vetor pos pos pos que contenha apenas os valores inteiros positivos de vet vet vet. A partir do vetor pos pos pos, deve ser gerado um outro vetor semdup semdup semdup que contenha apenas uma ocorrência de cada valor de pos pos pos. A saída do programa deve ser composta apenas pelos elementos de semdup semdup semdup separados por um espaço.

'''

vet = [int(i) for i in input().split()]
pos = []
semdup = []
for i in vet:
    if i >= 0:
        pos.append(i)
for i in pos:
    if str(i) not in semdup:
        semdup.append(str(i))
print(' '.join(semdup))
